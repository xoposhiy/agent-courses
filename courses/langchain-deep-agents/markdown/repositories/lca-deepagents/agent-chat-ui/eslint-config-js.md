# Official course repository: Python, TypeScript, lesson sources, and agent UI: agent-chat-ui/eslint.config.js

[Course index](../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/agent-chat-ui/eslint.config.js) · [Raw file](../../../../raw/repositories/lca-deepagents/agent-chat-ui/eslint.config.js)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```js
import js from "@eslint/js";
import globals from "globals";
import reactHooks from "eslint-plugin-react-hooks";
import reactRefresh from "eslint-plugin-react-refresh";
import tseslint from "typescript-eslint";

export default tseslint.config(
  { ignores: ["dist"] },
  {
    extends: [js.configs.recommended, ...tseslint.configs.recommended],
    files: ["**/*.{ts,tsx}"],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
    },
    plugins: {
      "react-hooks": reactHooks,
      "react-refresh": reactRefresh,
    },
    rules: {
      ...reactHooks.configs.recommended.rules,
      "@typescript-eslint/no-explicit-any": 0,
      "@typescript-eslint/no-unused-vars": [
        "warn",
        { args: "none", argsIgnorePattern: "^_", varsIgnorePattern: "^_" },
      ],
      "react-refresh/only-export-components": [
        "warn",
        { allowConstantExport: true },
      ],
    },
  },
);

```
