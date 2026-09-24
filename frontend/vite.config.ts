import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// L'aperçu live est servi derrière un hôte proxyé : on accepte tout hôte et on
// relaie /api vers le backend local. Le navigateur n'appelle jamais localhost.
export default defineConfig({
  plugins: [react()],
  server: {
    host: "0.0.0.0",
    port: 5173,
    strictPort: false,
    allowedHosts: true,
    proxy: {
      "/api": {
        target: "http://127.0.0.1:8000",
        changeOrigin: true,
      },
    },
  },
  preview: {
    host: "0.0.0.0",
    port: 4173,
    allowedHosts: true,
    proxy: {
      "/api": { target: "http://127.0.0.1:8000", changeOrigin: true },
    },
  },
  build: { outDir: "dist", sourcemap: true },
});
