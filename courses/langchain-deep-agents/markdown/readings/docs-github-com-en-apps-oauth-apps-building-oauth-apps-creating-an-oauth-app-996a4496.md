# Assigned reference: creating-an-oauth-app

[Course index](../../README.md) · [Original source](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app) · [Raw file](../../raw/readings/docs-github-com-en-apps-oauth-apps-building-oauth-apps-creating-an-oauth-app-996a4496.html)

Retrieved: 2026-11-13T17:00:51.296069+00:00

# Creating an OAuth app

You can create and register an OAuth app under your personal account or under any organization you have administrative access to. While creating your OAuth app, remember to protect your privacy by only using information you consider public.

Copy markdown

Note

Consider building a GitHub App instead of an OAuth app.

Both OAuth apps and GitHub Apps use OAuth 2.0.

OAuth apps can only act on behalf of a user while GitHub Apps can either act on behalf of a user or independently of a user.

GitHub Apps use fine-grained permissions, give the user more control over which repositories the app can access, and use short-lived tokens.

For more information, see [Differences between GitHub Apps and OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps) and [About creating GitHub Apps](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps).

Note

A user or organization can own up to 100 OAuth apps.

1. In the upper-right corner of any page on GitHub, click your profile picture, then click  **Settings**.
2. In the left sidebar, click  **Developer settings**.
3. In the left sidebar, click **OAuth apps**.
4. Click **New OAuth App**.

   Note

   If you haven't created an app before, this button will say, **Register a new application**.
5. In "Application name", type the name of your app.

   Warning

   Only use information in your OAuth app that you consider public. Avoid using sensitive data, such as internal URLs, when creating an OAuth app.
6. In "Homepage URL", type the full URL to your app's website.
7. Optionally, in "Application description", type a description of your app that users will see.
8. In "Authorization callback URL", type the callback URL of your app.

   You can enter up to 10 callback URLs. To add additional callback URLs, click **Add callback URL**.
9. If your OAuth app will use the device flow to identify and authorize users, click **Enable Device Flow**. For more information about the device flow, see [Authorizing OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps#device-flow).
10. **Expire user access tokens** is enabled by default. If your app's authentication code hasn't been updated to support short-lived tokens, uncheck the box until support is added. For more information about expiring tokens, see [Authorizing OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps#expiring-access-tokens).
11. Click **Register application**.

## [Further reading](docs-github-com-en-apps-oauth-apps-building-oauth-apps-creating-an-oauth-app-996a4496.md)

- [Modifying an OAuth app](https://docs.github.com/en/apps/oauth-apps/maintaining-oauth-apps/modifying-an-oauth-app)
