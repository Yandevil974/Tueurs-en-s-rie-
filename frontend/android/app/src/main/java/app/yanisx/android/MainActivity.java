package app.yanisx.android;

import android.content.res.AssetFileDescriptor;
import android.media.AudioAttributes;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.webkit.JavascriptInterface;
import android.webkit.WebSettings;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    private MediaPlayer mediaPlayer;

    public class NativeAudioInterface {
        @JavascriptInterface
        public void playAudio(String assetName) {
            runOnUiThread(() -> {
                try {
                    if (mediaPlayer != null) {
                        mediaPlayer.stop();
                        mediaPlayer.release();
                        mediaPlayer = null;
                    }

                    mediaPlayer = new MediaPlayer();
                    mediaPlayer.setAudioAttributes(new AudioAttributes.Builder()
                            .setUsage(AudioAttributes.USAGE_MEDIA)
                            .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
                            .build());

                    try {
                        AssetFileDescriptor afd = getAssets().openFd("public/audio/" + assetName);
                        mediaPlayer.setDataSource(afd.getFileDescriptor(), afd.getStartOffset(), afd.getLength());
                        afd.close();
                    } catch (Exception fdEx) {
                        java.io.File cacheFile = new java.io.File(getCacheDir(), assetName);
                        if (!cacheFile.exists() || cacheFile.length() == 0) {
                            java.io.InputStream in = getAssets().open("public/audio/" + assetName);
                            java.io.FileOutputStream out = new java.io.FileOutputStream(cacheFile);
                            byte[] buffer = new byte[8192];
                            int read;
                            while ((read = in.read(buffer)) != -1) {
                                out.write(buffer, 0, read);
                            }
                            out.flush();
                            out.close();
                            in.close();
                        }
                        mediaPlayer.setDataSource(cacheFile.getAbsolutePath());
                    }

                    mediaPlayer.prepare();
                    mediaPlayer.start();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            });
        }

        @JavascriptInterface
        public void pauseAudio() {
            runOnUiThread(() -> {
                if (mediaPlayer != null && mediaPlayer.isPlaying()) {
                    mediaPlayer.pause();
                }
            });
        }

        @JavascriptInterface
        public void resumeAudio() {
            runOnUiThread(() -> {
                if (mediaPlayer != null) {
                    mediaPlayer.start();
                }
            });
        }

        @JavascriptInterface
        public void stopAudio() {
            runOnUiThread(() -> {
                if (mediaPlayer != null) {
                    mediaPlayer.stop();
                    mediaPlayer.release();
                    mediaPlayer = null;
                }
            });
        }

        @JavascriptInterface
        public void seekTo(int sec) {
            runOnUiThread(() -> {
                if (mediaPlayer != null) {
                    mediaPlayer.seekTo(sec * 1000);
                }
            });
        }

        @JavascriptInterface
        public int getCurrentPosition() {
            if (mediaPlayer != null) {
                return mediaPlayer.getCurrentPosition() / 1000;
            }
            return 0;
        }

        @JavascriptInterface
        public boolean isPlaying() {
            return mediaPlayer != null && mediaPlayer.isPlaying();
        }
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        if (this.bridge != null && this.bridge.getWebView() != null) {
            WebSettings settings = this.bridge.getWebView().getSettings();
            settings.setMediaPlaybackRequiresUserGesture(false);
            this.bridge.getWebView().addJavascriptInterface(new NativeAudioInterface(), "AndroidNativeAudio");
        }
    }

    @Override
    public void onDestroy() {
        if (mediaPlayer != null) {
            mediaPlayer.release();
            mediaPlayer = null;
        }
        super.onDestroy();
    }
}
