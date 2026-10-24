package com.arenax.app;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.ContentResolver;
import android.content.ContentValues;
import android.content.Intent;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.util.Log;
import android.webkit.JavascriptInterface;
import android.webkit.JsResult;
import android.webkit.ValueCallback;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceRequest;
import android.webkit.WebResourceResponse;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;

import androidx.webkit.WebViewAssetLoader;

import java.io.File;
import java.io.FileOutputStream;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;

/**
 * ARENA//X — coque Android.
 *
 * L'application est entièrement embarquée dans les assets (arena-x.html) : elle
 * fonctionne hors ligne, sans serveur. Les fichiers sont servis par
 * WebViewAssetLoader sur une origine https, ce qui donne un vrai contexte
 * sécurisé : localStorage persistant et appels fetch vers les fournisseurs d'IA
 * sans blocage CORS.
 */
public class MainActivity extends Activity {

    private static final String TAG = "ARENA-X";
    private static final String START_URL = "https://appassets.androidplatform.net/assets/arena-x.html";
    private static final int REQ_FILE = 1001;

    private WebView web;
    private WebViewAssetLoader assetLoader;
    private ValueCallback<Uri[]> fileCallback;

    /** Pont injecté après le chargement : comble les manques du WebView. */
    private static final String SHIM =
        "(function(){" +
        "  if (window.__axBridge) return; window.__axBridge = 1;" +
        "  if (!window.ArenaAndroid) return;" +
        "  var blobs = {};" +
        "  var create = URL.createObjectURL;" +
        "  URL.createObjectURL = function(o){ var u = create.call(URL, o); blobs[u] = o; return u; };" +
        "  document.addEventListener('click', function(e){" +
        "    var a = e.target && e.target.closest ? e.target.closest('a[download]') : null;" +
        "    if (!a) return;" +
        "    var href = a.getAttribute('href') || '';" +
        "    var blob = blobs[href];" +
        "    if (blob && blob.text) {" +
        "      e.preventDefault(); e.stopPropagation();" +
        "      blob.text().then(function(t){" +
        "        window.ArenaAndroid.saveFile(a.getAttribute('download') || 'arena-x.json', t);" +
        "      });" +
        "    }" +
        "  }, true);" +
        "  try {" +
        "    navigator.share = function(d){" +
        "      if (!d || !d.files || !d.files.length) return Promise.reject(new Error('partage non disponible'));" +
        "      var f = d.files[0];" +
        "      return f.text().then(function(t){ window.ArenaAndroid.saveFile(f.name || 'arena-x.json', t); });" +
        "    };" +
        "    navigator.canShare = function(d){ return !!(d && d.files && d.files.length); };" +
        "  } catch (err) {}" +
        "})();";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        assetLoader = new WebViewAssetLoader.Builder()
                .addPathHandler("/assets/", new WebViewAssetLoader.AssetsPathHandler(this))
                .build();

        web = new WebView(this);
        web.setBackgroundColor(0xFF05060A);

        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true);
        s.setDatabaseEnabled(true);
        s.setSupportZoom(false);
        s.setBuiltInZoomControls(false);
        s.setUseWideViewPort(false);
        s.setLoadWithOverviewMode(false);
        s.setMediaPlaybackRequiresUserGesture(false);
        s.setJavaScriptCanOpenWindowsAutomatically(true);
        s.setUserAgentString(s.getUserAgentString() + " ArenaXApp/1.0");

        web.setWebViewClient(new WebViewClient() {
            @Override
            public WebResourceResponse shouldInterceptRequest(WebView view, WebResourceRequest request) {
                return assetLoader.shouldInterceptRequest(request.getUrl());
            }

            @Override
            public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
                Uri uri = request.getUrl();
                if (uri != null && "appassets.androidplatform.net".equals(uri.getHost())) return false;
                /* Liens externes (clés API, crédits, dépôt) : navigateur du téléphone. */
                try { startActivity(new Intent(Intent.ACTION_VIEW, uri)); }
                catch (Exception e) { Log.w(TAG, "lien externe non ouvrable: " + uri, e); }
                return true;
            }

            @Override
            public void onPageFinished(WebView view, String url) {
                view.evaluateJavascript(SHIM, null);
            }
        });

        web.setWebChromeClient(new WebChromeClient() {
            @Override
            public boolean onJsAlert(WebView view, String url, String message, final JsResult result) {
                new AlertDialog.Builder(MainActivity.this)
                        .setMessage(message)
                        .setPositiveButton(android.R.string.ok, (d, w) -> result.confirm())
                        .setOnCancelListener(d -> result.cancel())
                        .show();
                return true;
            }

            @Override
            public boolean onJsConfirm(WebView view, String url, String message, final JsResult result) {
                new AlertDialog.Builder(MainActivity.this)
                        .setMessage(message)
                        .setPositiveButton(android.R.string.ok, (d, w) -> result.confirm())
                        .setNegativeButton(android.R.string.cancel, (d, w) -> result.cancel())
                        .setOnCancelListener(d -> result.cancel())
                        .show();
                return true;
            }

            @Override
            public boolean onShowFileChooser(WebView view, ValueCallback<Uri[]> callback, FileChooserParams params) {
                fileCallback = callback;
                Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
                intent.addCategory(Intent.CATEGORY_OPENABLE);
                intent.setType("*/*");
                try {
                    startActivityForResult(Intent.createChooser(intent, "Choisir une sauvegarde JSON"), REQ_FILE);
                    return true;
                } catch (Exception e) {
                    fileCallback = null;
                    Toast.makeText(MainActivity.this, "Aucune application de fichiers trouvée.", Toast.LENGTH_LONG).show();
                    return false;
                }
            }
        });

        /* Téléchargements http(s) éventuels (aucun aujourd'hui, mais sans risque). */
        web.setDownloadListener((url, userAgent, contentDisposition, mimeType, length) -> {
            try { startActivity(new Intent(Intent.ACTION_VIEW, Uri.parse(url))); }
            catch (Exception ignored) { }
        });

        web.addJavascriptInterface(new Bridge(), "ArenaAndroid");
        setContentView(web);
        web.loadUrl(START_URL);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == REQ_FILE) {
            Uri[] result = null;
            if (resultCode == RESULT_OK && data != null && data.getData() != null) {
                result = new Uri[]{data.getData()};
            }
            if (fileCallback != null) {
                fileCallback.onReceiveValue(result);
                fileCallback = null;
            }
            return;
        }
        super.onActivityResult(requestCode, resultCode, data);
    }

    @Override
    public void onBackPressed() {
        if (web != null && web.canGoBack()) {
            web.goBack();
            return;
        }
        super.onBackPressed();
    }

    @Override
    protected void onPause() {
        if (web != null) web.onPause();
        super.onPause();
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (web != null) web.onResume();
    }

    /** API exposée au JavaScript sous le nom window.ArenaAndroid. */
    public class Bridge {

        @JavascriptInterface
        public String platform() {
            return "android";
        }

        @JavascriptInterface
        public String version() {
            return "1.0";
        }

        /**
         * Écrit un fichier texte dans les Téléchargements du téléphone.
         * Remplace le téléchargement blob du navigateur, absent du WebView.
         */
        @JavascriptInterface
        public void saveFile(final String name, final String text) {
            final String safe = (name == null || name.trim().isEmpty())
                    ? "arena-x.json"
                    : name.replaceAll("[^A-Za-z0-9._-]", "_");
            final String body = text == null ? "" : text;

            runOnUiThread(() -> {
                try {
                    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
                        ContentValues values = new ContentValues();
                        values.put(MediaStore.Downloads.DISPLAY_NAME, safe);
                        values.put(MediaStore.Downloads.MIME_TYPE, "application/json");
                        values.put(MediaStore.Downloads.IS_PENDING, 1);
                        ContentResolver resolver = getContentResolver();
                        Uri uri = resolver.insert(MediaStore.Downloads.EXTERNAL_CONTENT_URI, values);
                        if (uri == null) throw new IllegalStateException("écriture refusée");
                        try (OutputStream out = resolver.openOutputStream(uri)) {
                            if (out != null) out.write(body.getBytes(StandardCharsets.UTF_8));
                        }
                        values.clear();
                        values.put(MediaStore.Downloads.IS_PENDING, 0);
                        resolver.update(uri, values, null, null);
                        Toast.makeText(MainActivity.this, "Enregistré dans Téléchargements : " + safe, Toast.LENGTH_LONG).show();
                    } else {
                        File dir = getExternalFilesDir(Environment.DIRECTORY_DOWNLOADS);
                        if (dir == null) dir = getFilesDir();
                        File file = new File(dir, safe);
                        try (FileOutputStream out = new FileOutputStream(file)) {
                            out.write(body.getBytes(StandardCharsets.UTF_8));
                        }
                        Toast.makeText(MainActivity.this, "Enregistré : " + file.getAbsolutePath(), Toast.LENGTH_LONG).show();
                    }
                } catch (Exception e) {
                    Log.e(TAG, "saveFile a échoué", e);
                    Toast.makeText(MainActivity.this, "Échec de l'enregistrement : " + e.getMessage(), Toast.LENGTH_LONG).show();
                }
            });
        }
    }
}
