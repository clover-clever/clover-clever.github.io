# Stash Blog Implementation Plan

> **For agentic workers:** Use the approved design brief and execute the implementation tasks continuously; independent text/style work may run in parallel, followed by a full change review.

**Goal:** Publish the approved Chirpy + Mocha blog with clear collections and a reusable writing workflow.

**Architecture:** Retain the Chirpy 7.6 starter and its existing GitHub Actions deployment. Override the official stylesheet and only the layouts/includes needed for branding and empty collections.

**Tech Stack:** Jekyll, Liquid, Sass, Markdown, GitHub Pages/Actions.

**Spec:** docs/superpowers/specs/2026-10-06-stash-blog.md

## Global Constraints
- Exact approved title and subtitle; fixed Catppuccin Mocha.
- lang: ko-KR; timezone: Asia/Seoul; baseurl: ""; author: MOSFET Thief.
- Two category levels; unpublished technical draft must not appear on the live site.
- Preserve the original Gemfile and workflow.
- Existing GitHub main commit: ccc3de99e2e02d4544d46a468742c9b1e939542a.
- Work in an isolated local snapshot; publish atomically with a checked expected branch head.

## Review Focus
- Long title and Korean navigation must wrap without horizontal overflow.
- Empty categories must display their names without links to nonexistent archives.
- Future published posts must retain normal pagination, search and category behavior.
- About-page math and local icon paths must resolve in the deployed site.
- Draft content and documentation must stay out of generated public routes.

## Task 1: Branding, collections and writing foundation
**Files:** _config.yml, _data/contact.yml, _data/stash.yml, _includes/sidebar.html, _includes/favicons.html, _includes/stash-collections.html, _includes/stash-intro.html, _layouts/home.html, _layouts/categories.html, assets/css/jekyll-theme-chirpy.scss, assets/img/stash-mark.svg, assets/img/favicons/*, _tabs/about.md, README.md, docs/templates/post.md, _drafts/rl-circuit-current-response.md.
**Consumes:** Official Chirpy 7.6 layouts and stylesheet entry.
**Produces:** A complete site source tree with approved identity and unpublished draft.
- [x] Confirm repository access and initial successful Build and Deploy.
- [x] Materialize an isolated source snapshot and verify its Git tree equals the remote tree.
- [x] Apply site configuration and original local icon.
- [x] Add compact home introduction and data-driven two-level collection overview.
- [x] Add Mocha CSS and syntax colors; preserve official stylesheet entry.
- [x] Add About, writing template, README and first RL draft.
- [x] Parse YAML/front matter and review Liquid, assets, and changes for secrets/placeholders.

## Task 2: Review, deploy and verify
**Files:** Changed site files from Task 1.
**Consumes:** Reviewed local source tree and current remote branch head.
**Produces:** Verified GitHub Pages deployment.
- [x] Review the complete diff independently and fix material issues.
- [ ] Publish one atomic Git tree/commit with a checked expected_sha.
- [ ] Confirm Actions build, HTML validation and deployment succeed for that commit.
- [ ] Inspect the live homepage, categories and About; check math, styles and paths.
- [ ] Report actual completed work and any specific unverified aspect.

## Verification decisions
This is primarily reversible configuration, styling and content. Use structural validation, the existing Jekyll/HTML-proofer build, and live browser inspection instead of implementation-mirroring unit tests. Ruby is not installed locally; GitHub Actions is the authoritative Jekyll build.
