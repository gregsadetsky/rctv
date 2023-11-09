import { resolve } from "path";

export default {
  plugins: [],
  root: resolve("./src"),
  base: "/static/",
  envDir: "../../../",
  resolve: {
    extensions: [".js", ".jsx", '.ts', '.tsx']
  },
  build: {
    sourcemap: true,
    outDir: resolve("../static/js/dist"),
    assetsDir: "",
    manifest: true,
    emptyOutDir: true,
    target: "es2020",
    rollupOptions: {
      input: {
        app: resolve("./src/app.ts"),
      },
      output: {
        chunkFileNames: undefined
      }
    }
  },
};
