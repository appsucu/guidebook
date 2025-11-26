# Типографіка

<div style="text-align: center; margin: 2rem 0;">
  <img src="/guidebook/assets/logo/brandpng/fonts.png" alt="APPS UCU Fonts" style="max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);">
</div>

Типографіка є ключовим елементом візуальної ідентичності Факультету прикладних наук УКУ. Правильне використання шрифтів забезпечує впізнаваність бренду та професійний вигляд усіх комунікаційних матеріалів.

---

## Основний шрифт

### Inter

<div class="font-showcase" style="font-family: 'Inter', sans-serif; margin: 2rem 0;">
  <p style="font-size: 3rem; font-weight: 800; letter-spacing: -0.02em; margin: 0;">Inter ExtraBold</p>
  <p style="font-size: 2rem; font-weight: 500; margin: 0.5rem 0;">Inter Medium</p>
  <p style="font-size: 1.25rem; font-weight: 400; margin: 0;">Inter Regular</p>
</div>

**Inter** — сучасний безсерифний шрифт з відкритим кодом, розроблений Расмусом Андерссоном спеціально для екранних інтерфейсів. Відрізняється чудовою читабельністю на будь-яких розмірах та підтримує кириличні символи.

[:fontawesome-solid-download: Завантажити Inter](https://fonts.google.com/specimen/Inter){ .md-button .md-button--primary }

---

## Ієрархія шрифтів

### Заголовки першого рівня

<div class="type-example" style="background: none; color: white; padding: 2rem; border-radius: 12px; margin: 1.5rem 0;">
  <p style="font-family: 'Inter', sans-serif; font-size: 2.5rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">COFFEE & DATA SCIENCE</p>
</div>

| Параметр | Значення |
|----------|----------|
| **Гарнітура** | Inter |
| **Накреслення** | ExtraBold (800) |
| **Регістр** | Верхній (UPPERCASE) |
| **Трекінг** | +50 (0.05em) |

```css
font-family: 'Inter', sans-serif;
font-weight: 800;
text-transform: uppercase;
letter-spacing: 0.05em;
```

---

### Заголовки другого рівня

<div class="type-example" style="background: #none; padding: 2rem; border-radius: 12px; border: 1px solid #e5e7eb; margin: 1.5rem 0;">
  <p style="font-family: 'Inter', sans-serif; font-size: 1.5rem; font-weight: 500; color: #1a1a1aff; margin: 0;">Master's Symposium on Advances in Data Mining, Machine Learning, and Computer Vision</p>
</div>

| Параметр | Значення |
|----------|----------|
| **Гарнітура** | Inter |
| **Накреслення** | Medium (500) |
| **Регістр** | Звичайний (Sentence case) |
| **Трекінг** | 0 |

```css
font-family: 'Inter', sans-serif;
font-weight: 500;
```

---

### Основний текст

<div class="type-example" style="background: none; padding: 2rem; border-radius: 12px; border: 1px solid #e5e7eb; margin: 1.5rem 0;">
  <p style="font-family: 'Inter', sans-serif; font-size: 1rem; font-weight: 400; color: #2a2a2aff; line-height: 1.7; margin: 0;">Факультет прикладних наук Українського католицького університету готує фахівців у галузі комп'ютерних наук, аналітики даних та штучного інтелекту. Наші випускники працюють у провідних технологічних компаніях світу.</p>
</div>

| Параметр | Значення |
|----------|----------|
| **Гарнітура** | Inter |
| **Накреслення** | Regular (400) |
| **Інтерліньяж** | 1.6–1.7 |
| **Колір** | Dark Gray (#58595b) |

```css
font-family: 'Inter', sans-serif;
font-weight: 400;
line-height: 1.7;
color: #58595b;
```

---

## Альтернативний шрифт

### Exo 2

<div class="font-showcase" style="font-family: 'Exo 2', sans-serif; margin: 2rem 0;">
  <p style="font-size: 2.5rem; font-weight: 800; margin: 0;">Exo 2 ExtraBold</p>
</div>

Шрифт **Exo 2** використовується як альтернатива для презентацій та акцентних заголовків, коли потрібен більш технологічний, футуристичний вигляд.

[:fontawesome-solid-download: Завантажити Exo 2](https://fonts.google.com/specimen/Exo+2){ .md-button }

---

## Специфікації розмірів

### Для веб-застосунків

| Елемент | Шрифт | Вага | Розмір | Інтерліньяж |
|---------|-------|------|--------|-------------|
| **H1** | Inter | ExtraBold (800) | 48px | 1.1 |
| **H2** | Inter | ExtraBold (800) | 36px | 1.2 |
| **H3** | Inter | Medium (500) | 24px | 1.3 |
| **H4** | Inter | Medium (500) | 20px | 1.4 |
| **Body** | Inter | Regular (400) | 16px | 1.7 |
| **Small** | Inter | Regular (400) | 14px | 1.5 |
| **Caption** | Inter | Regular (400) | 12px | 1.4 |

### Для друкованих матеріалів

| Елемент | Шрифт | Вага | Розмір | Інтерліньяж |
|---------|-------|------|--------|-------------|
| **H1** | Inter | ExtraBold (800) | 36pt | 40pt |
| **H2** | Inter | ExtraBold (800) | 24pt | 28pt |
| **H3** | Inter | Medium (500) | 18pt | 22pt |
| **Body** | Inter | Regular (400) | 11pt | 14pt |
| **Caption** | Inter | Regular (400) | 9pt | 11pt |

---

## Підключення шрифтів

=== "HTML"

    ```html
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;800&display=swap" rel="stylesheet">
    ```

=== "CSS"

    ```css
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;800&display=swap');

    body {
      font-family: 'Inter', sans-serif;
    }
    ```

=== "Figma / Sketch"

    Завантажте шрифт локально та встановіть у систему:
    
    1. Перейдіть на [Google Fonts](https://fonts.google.com/specimen/Inter)
    2. Натисніть "Download family"
    3. Розпакуйте архів та встановіть файли `.ttf`

---

## Правила використання

!!! success "Рекомендовано"
    - Використовуйте Inter для всіх офіційних матеріалів
    - Дотримуйтесь ієрархії ваг шрифту
    - Забезпечуйте достатній контраст тексту
    - Використовуйте uppercase тільки для коротких заголовків

!!! warning "Уникайте"
    - Не використовуйте більше 3 різних ваг на одній сторінці
    - Не розтягуйте та не стискайте шрифт
    - Не використовуйте занадто малий розмір (менше 12px для веб)
    - Не змішуйте Inter з іншими безсерифними шрифтами

!!! danger "Заборонено"
    - Заміна Inter на інші шрифти в офіційних документах
    - Використання декоративних або рукописних шрифтів
    - Зміна пропорцій літер
