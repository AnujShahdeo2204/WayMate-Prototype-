---
name: "WayMate — Warm Editorial Mobility"
description: "Minimalist black-and-beige design system for WayMate, an airport ride-sharing and passenger pooling Android application."
---

## Overview

WayMate's visual identity is built on calm, trustworthy clarity for air travellers landing in unfamiliar or busy cities. A warm beige canvas paired with crisp cream cards and deep charcoal-black primary actions eliminates visual noise, making flight-based pooling, luggage compatibility, and post-ride payments effortless to scan under travel fatigue.

The design style is **Warm Minimalism** tailored for native Android (Material 3 / Jetpack Compose): flat tonal surfaces, 1px hairline borders, generous touch targets, and restrained functional motion.

## Colors

The palette preserves WayMate's signature black-and-beige direction, avoiding bright neon hues, gradients, or glassmorphism.

- **Primary Black (`#1C1B18`):** Reserved for primary calls to action, active navigation states, and key focal anchors.
- **Warm Beige (`#F3EBDD`) & Cream (`#FAF7F0`):** Primary screen ground and elevated card surfaces that reduce glare and feel grounded.
- **Secondary Beige (`#E8DDCA`) & Border (`#D8CEBD`):** Subtle tonal separation for chips, input wells, and hairline dividers.
- **Semantic Status:** Muted sage green (`#526B50`) for confirmed pools and completed journeys; muted terracotta (`#A34D40`) for cancellations, errors, and SOS alerts.

```yaml
colors:
  primary: "#1C1B18"
  on-primary: "#FAF7F0"
  primary-hover: "#32302D"
  surface: "#F3EBDD"
  on-surface: "#24231F"
  surface-card: "#FAF7F0"
  on-surface-card: "#24231F"
  surface-secondary: "#E8DDCA"
  on-surface-secondary: "#24231F"
  surface-muted: "#E9E2D4"
  secondary-text: "#5E594F"
  border: "#D8CEBD"
  border-strong: "#B1AA9E"
  success: "#526B50"
  on-success: "#FAF7F0"
  success-container: "#DCF9D6"
  on-success-container: "#1F361F"
  error: "#A34D40"
  on-error: "#FAF7F0"
  error-container: "#FFEDEA"
  on-error-container: "#5C1810"
```

## Typography

A three-role Google Font hierarchy pairs **Red Hat Text** for geometric clarity in headings with **Instrument Sans** for legible UI body copy and **Spline Sans Mono** for flight codes, OTP digits, vehicle registration numbers, and tabular fares.

```yaml
typography:
  display-lg:
    fontFamily: "Red Hat Text"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 42px
    letterSpacing: -0.5px
  display-lg-mobile:
    fontFamily: "Red Hat Text"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 34px
    letterSpacing: -0.3px
  headline-lg:
    fontFamily: "Red Hat Text"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 30px
    letterSpacing: -0.25px
  headline-md:
    fontFamily: "Red Hat Text"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 26px
    letterSpacing: -0.15px
  title-md:
    fontFamily: "Instrument Sans"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 22px
    letterSpacing: 0px
  body-md:
    fontFamily: "Instrument Sans"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
    letterSpacing: 0px
  body-sm:
    fontFamily: "Instrument Sans"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 17px
    letterSpacing: 0.1px
  label-lg:
    fontFamily: "Instrument Sans"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 20px
    letterSpacing: 0.1px
  label-sm:
    fontFamily: "Instrument Sans"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 16px
    letterSpacing: 0.4px
  mono-md:
    fontFamily: "Spline Sans Mono"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
    letterSpacing: 0.2px
  mono-sm:
    fontFamily: "Spline Sans Mono"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 16px
    letterSpacing: 0.2px
```

## Layout & Spacing

Designed for a 390px Android mobile viewport using a single-column fluid layout with 20px horizontal page margins and a strict 4px/8px spacing rhythm. Touch targets (buttons, stepper controls, list rows, bottom navigation tabs) maintain a minimum height of 48px.

```yaml
spacing:
  gutter-xs: 4px
  gutter-sm: 8px
  gutter-md: 12px
  gutter-lg: 16px
  gutter-xl: 24px
  section: 32px
  page-margin: 20px
```

## Elevation & Depth

Hierarchy relies on **tonal layering and subtle 1px borders (`#D8CEBD`)** rather than heavy drop shadows. Cream cards (`#FAF7F0`) sit on the warm beige ground (`#F3EBDD`). Shadows are minimal or omitted; active floating elements (such as bottom sheets on live tracking maps) use a single soft hairline border and subtle ambient lift.

## Shapes

Generous, friendly Android-native rounded corners soften the high-contrast black-and-beige palette. Cards use `16px` (`lg`), inputs and secondary tiles use `12px` (`md`), primary pill/rounded buttons use `12px` (`md`) or `full`, and status badges use `9999px` (`full`).

```yaml
rounded:
  sm: 6px
  DEFAULT: 10px
  md: 12px
  lg: 16px
  xl: 24px
  full: 9999px
```

## Motion & Micro-interaction

Motion is understated, functional, and free of decorative loops. Button presses and chip selections respond immediately (`100ms`); matching progress indicators use a subtle linear bar or calm pulse without heavy animation.

```yaml
motion:
  state-change:
    duration: 120ms
    delay: 0ms
    timingFunction: ease-out
  surface-enter:
    duration: 220ms
    delay: 0ms
    timingFunction: cubic-bezier(0.2, 0, 0, 1)
  surface-exit:
    duration: 150ms
    delay: 0ms
    timingFunction: cubic-bezier(0.3, 0, 1, 1)
```

## Voice & Content Strategy

- **Tone:** Calm, clear, and reassuring—written for travellers managing flights and luggage.
- **Capitalisation:** Sentence case for headings, labels, and body copy; uppercase reserved only for airport IATA codes (`DEL`, `BOM`, `BLR`) and short status tags.
- **Terminology:** Always say **Pool** (not "carpool group"), **Shared Ride** / **Solo Ride**, **Final Destination**, and **Boot Space** (for luggage capacity).
- **Formatting:** Indian Rupee (`₹`) with `tabular-nums` (`₹400`, `₹1,200`), 12-hour clock with AM/PM (`10:30 AM`), and Indian mobile format (`+91 98765 43210`).

## Components

Component implementations live as individual HTML sticker sheet files in
`components/`. Each file contains the canonical, styled HTML components with
`<!-- COMPONENT: name -->` comment markers. Read each file before use.

- **Badge** → `@components/badge.html` — `badge-numeric`, `badge-dot`
- **Button** → `@components/button.html` — `button-primary`, `button-icon`, `button-with-icon`
- **Card** → `@components/card.html` — `card-elevated`, `card-action`, `card-interactive`, `card-interactive-2`
- **Input Field** → `@components/input-field.html` — `input-field-text`, `input-field-icon`
- **Stepper** → `@components/stepper.html` — `stepper-standard`, `stepper-invalid`
