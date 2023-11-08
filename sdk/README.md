# JS SDK ? 

This script can be included by developers who want to use the Recruse API from
their RCTV apps.

```html
<head>
    <!-- Defer scripts only executed after the document has been loaded -->
    <script defer src="rctv.recurse.com/app-sdk.js">
</head>

```

## Development Setup


### Install

```sh
# Linux
curl -fsSL https://bun.sh/install | bash # for macOS, Linux, and WSL

# Homebrew (macOS)
brew tap oven-sh/bun

brew install bun
```

### Running 

Local development in watch mode


```sh 
# Watches for file changes, builds sdk, and places compiled JavaScript in static/app-sdk.js
bun watch

```

Use `bun` to build the final SDK js script.

```sh
# Builds sdk and places compiled JavaScript in static/app-sdk.js
bun bundle 
```

