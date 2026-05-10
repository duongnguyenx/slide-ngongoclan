# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A single-page HTML slide deck for a Vietnamese cosmetology graduation thesis (Đồ án tốt nghiệp 2026, Cao đẳng Việt Mỹ Hà Nội) on treating closed-comedone acne (mụn ẩn). Content is in Vietnamese — keep all user-facing copy in Vietnamese.

There is no build system, no package manager, no tests. The whole deck is `index.html` (~2100 lines) with inline `<style>` and `<script>` blocks.

## Running / previewing

- Open `index.html` directly in a browser. No dev server needed — Tailwind, Lucide, and Google Fonts load from CDNs.
- Navigation: `→` / `Space` next, `←` previous, or use the on-screen buttons (bottom right).
- Print to PDF: the `@media print` block at `index.html:488` sets `@page { size: 16in 9in }` (16:9 landscape). Use the browser's "Save as PDF" with default margins.

## Architecture

**Slides are positional, not keyed.** The runtime in `index.html:2088` does `document.querySelectorAll(".slide")` and tracks `currentSlide` as an array index. To add/remove/reorder a slide, just move its `<div class="slide …">` block inside `<div id="presentation">` — there are no IDs to update. Slides are commented in source order (`<!-- Slide 1: Bìa -->` through `<!-- Slide 17: Cảm ơn -->`); keep these comments in sync if you reorder.

**Visibility is class-driven.** Only the slide with `.active` is shown — the base `.slide` rule is `position: absolute; opacity: 0; visibility: hidden`, and `.slide.active` flips it to `position: relative; opacity: 1`. Don't rely on `display: none`; entry animations key off `.slide.active` selectors (see `index.html:439`–`485`).

**Slide counter hardcoded value is stale.** `<div id="slideCounter">1 / 10</div>` at `index.html:2078` is overwritten by JS on load with the real `${currentSlide + 1} / ${slides.length}`. Don't bother updating the literal "1 / 10" — but be aware the deck currently has 17 slides, not 10.

**Two background variants alternate by design.** `.bg-teal-slide` and `.bg-blue-slide` are toggled slide-by-slide for visual rhythm. Color tokens live as CSS variables in `:root` (`--teal`, `--blue`, `--yellow`, `--red`) at `index.html:14` — change colors there, not in individual slides.

**Animations split into idle vs. entry.** Idle classes (`idle-pulse`, `idle-glow`, `idle-shimmer`, `idle-float`, `cadi-bar-animated`) loop continuously. Entry animations are scoped behind `.slide.active` and only run when the slide becomes visible — staggered `nth-child` delays on `<li>` produce the cascade effect. If a new element should animate on entry, match the existing `.slide.active <selector>` patterns.

## Companion script

`Bai_Thuyet_Trinh_Noi.md` is the spoken narration (~15–20 min, slide-by-slide) that pairs with the deck. If you change a slide's content meaningfully, update the matching `## 🎤 SLIDE N` section so the spoken script stays consistent with what's on screen.

## Assets

- `asset/1.png` … `asset/10.png` — slide imagery, referenced by relative path.
- `media/` — videos (`video01.mov`, `video02.mov`) embedded in slides 6 and 15, plus client photos.
- `DoAn_NgoNgocLan_2026.docx` — the full written thesis (source-of-truth for facts cited in slides); not used at runtime.
