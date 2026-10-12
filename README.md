# MOSFET Thief's Stash

**Whatever sparks curiosity**

My personal site for notes on motor control, power electronics, embedded systems, and other things I find interesting. Built with Jekyll Chirpy and the Catppuccin Mocha color palette.

## Writing and publishing

| Path | What goes here |
| --- | --- |
| `_drafts/` | Unpublished drafts |
| `_posts/` | Published articles |
| `_tabs/about.md` | About page |
| `_tabs/projects.md` | Projects page |
| `docs/templates/post.md` | Post template |
| `assets/img/posts/` | Images for posts |

The first planned series goes from RL circuits to PMSM current control. The draft is in `_drafts/rl-circuit-current-response.md`. The `_posts/2026-10-06-tbd.md` placeholder remains unpublished.

## Categories

| Main category | Subcategory |
| --- | --- |
| Motor Control & Power Electronics | Motor Drives |
| Motor Control & Power Electronics | Converters |
| Other Topics | Mathematics |
| Other Topics | Physics & Science |
| Reflections | None |

Use both categories in the post's front matter, for example:

```yaml
categories: ["Motor Control & Power Electronics", "Motor Drives"]
```

## Before publishing

1. Copy `docs/templates/post.md` into `_drafts/` and write the article.
2. Keep `published: false` until the draft is ready. Check equations, units, assumptions, references, and any claims of experimental results.
3. Move the file to `_posts/YYYY-MM-DD-slug.md`, set the publication date, and remove `published: false`.
4. Commit and push the change. Check GitHub Actions for a successful Pages build, then review the live article, including links, equations, and mobile layout.

**Drafts committed to a public repository are still publicly readable on GitHub.** Don't add private notes, personal data, or material you aren't allowed to publish.

## Math and Obsidian

Set `math: true` in the post front matter. Chirpy uses `$$...$$` for both inline and display math. Leave blank lines around display equations and check their rendering on the live site.

When importing from Obsidian, replace wiki-links and embeds with normal Markdown links and images. Move images into the repository, update their paths, and check any plugin-specific syntax.

## Links

- [Chirpy's writing guide](https://chirpy.cotes.page/posts/write-a-new-post/)
- [License](LICENSE)
