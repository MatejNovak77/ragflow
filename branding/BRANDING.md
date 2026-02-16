# BYZZARD Branding Guide

This document describes how to re-apply BYZZARD branding after an upstream RAGFlow merge. The branding replaces user-visible "RAGFlow" references with "BYZZARD" and swaps the logo with the BYZKIDS logo.

## Quick Reference

| File | Change |
|---|---|
| `web/public/logo.svg` | Replace with `branding/logo.svg` (BYZKIDS logo) |
| `web/src/conf.json` | `"appName": "RAGFlow"` → `"appName": "BYZZARD"` |
| `web/index.html` | `<title>RAGFlow</title>` → `<title>BYZZARD</title>` |
| `web/src/pages/login-next/index.tsx` | `RAGFlow` brand text → `BYZZARD` |
| `web/src/pages/admin/login.tsx` | `RAGFlow` brand text → `BYZZARD` |
| `web/src/pages/home/banner.tsx` | `Welcome to RAGFlow` → `Welcome to BYZZARD`; gradient text `RAGFlow` → `BYZZARD` |
| `web/src/pages/next-search/search-home.tsx` | `RAGFlow` heading → `BYZZARD` |
| `web/src/components/embed-container.tsx` | Move logo to center of top bar, remove appName text |
| `web/src/pages/next-chats/share/index.tsx` | Add `useEffect` setting `document.title = 'BYZZARD'` |
| `web/src/layouts/next-header.tsx` | Remove Discord link, GitHub link, and ragflow.io docs help button |

## Detailed Instructions

### 1. Logo Replacement

Copy `branding/logo.svg` to `web/public/logo.svg`:

```bash
cp branding/logo.svg web/public/logo.svg
```

### 2. App Name and Page Title

**`web/src/conf.json`** — Change appName:
```json
// Before:
{ "appName": "RAGFlow" }
// After:
{ "appName": "BYZZARD" }
```

**`web/index.html`** — Change `<title>`:
```html
<!-- Before: -->
<title>RAGFlow</title>
<!-- After: -->
<title>BYZZARD</title>
```

### 3. Login Page

**`web/src/pages/login-next/index.tsx`** — Find the brand text next to the logo image. Look for a `<div>` with text "RAGFlow" near `<img src={'/logo.svg'}`:
```tsx
// Before:
<div className="text-xl font-bold self-center">RAGFlow</div>
// After:
<div className="text-xl font-bold self-center">BYZZARD</div>
```

### 4. Admin Login Page

**`web/src/pages/admin/login.tsx`** — Find the brand text next to the logo. Look for `<span>` with "RAGFlow" near `<img ... src="/logo.svg"`:
```tsx
// Before:
<span className="text-xl font-bold">RAGFlow</span>
// After:
<span className="text-xl font-bold">BYZZARD</span>
```

### 5. Home Page Banner

**`web/src/pages/home/banner.tsx`** — Two changes:

1. In the `Banner` component, find the welcome text:
```tsx
// Before:
Welcome to RAGFlow
// After:
Welcome to BYZZARD
```

2. In the `NextBanner` component, find the gradient-styled brand text:
```tsx
// Before:
RAGFlow
// After:
BYZZARD
```

### 6. Search Page Heading

**`web/src/pages/next-search/search-home.tsx`** — Find the gradient heading in the `<h1>`:
```tsx
// Before:
RAGFlow
// After:
BYZZARD
```

### 7. Embedded Chat Container

**`web/src/components/embed-container.tsx`** — Restructure the top bar:

1. Remove the absolute-positioned logo+appName `<div>` that sits outside the main card
2. Add a centered logo inside the top bar (between the avatar/title and the Reset button):
```tsx
<div className="flex-1 flex justify-center">
  <img src="/logo.svg" alt="BYZKIDS" className="h-8 w-auto" />
</div>
```
3. Remove `useFetchAppConf` import and usage since `appConf.appName` is no longer displayed

### 8. Shared Chat Page Title

**`web/src/pages/next-chats/share/index.tsx`** — Add a `useEffect` to set the document title:
```tsx
React.useEffect(() => {
  document.title = 'BYZZARD';
}, []);
```

### 9. Header — Remove External Links

**`web/src/layouts/next-header.tsx`** — Remove three elements:

1. **Discord link** — Remove the `<a>` tag linking to `https://discord.com/invite/...` with the Discord icon
2. **GitHub link** — Remove the `<a>` tag linking to `https://github.com/infiniflow/ragflow` with the GitHub icon
3. **Docs help button** — Remove the `handleDocHelpCLick` function and the `<Button>` with `<CircleHelp />` icon
4. **Clean up imports** — Remove `IconFontFill` and `CircleHelp` imports if no longer used

## Files NOT Modified (by design)

- **Internal component names** (`RAGFlowAvatar`, `RAGFlowForm`, etc.) — not user-visible, renaming causes massive merge conflicts
- **Locale/i18n files** (14 language files, ~95 references) — deep help text, rarely seen, high merge conflict risk
- **Backend/Docker** — no user-visible RAGFlow branding there

## Verification Checklist

After applying branding:

1. Login page shows BYZKIDS logo + "BYZZARD" text
2. Admin login page shows BYZKIDS logo + "BYZZARD" text
3. Home page banner says "Welcome to BYZZARD"
4. Home page NextBanner shows gradient "BYZZARD" text
5. Search page heading says "BYZZARD"
6. Browser tab title says "BYZZARD"
7. Header has no Discord, GitHub, or docs links
8. Embedded chat (share URL) shows BYZKIDS logo centered in top bar
9. Shared chat page tab title says "BYZZARD"
10. `conf.json` appName is "BYZZARD"
