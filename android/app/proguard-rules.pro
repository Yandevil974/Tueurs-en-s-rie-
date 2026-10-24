# L'interface JavaScript appelle ArenaAndroid.saveFile : ne pas renommer la classe.
-keepclassmembers class com.arenax.app.MainActivity$Bridge {
    public *;
}
-keepattributes JavascriptInterface
