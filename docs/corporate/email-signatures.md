# Email-підписи

Стандартизовані підписи електронної пошти забезпечують професійний вигляд комунікацій та впізнаваність бренду.

---

## Стандартний формат

<div style="background: #ffffff; border-left: 3px solid #662d91; padding: 1.5rem; margin: 2rem 0; font-family: Arial, sans-serif;">
  <p style="margin: 0; font-weight: 600; color: #662d91; font-size: 1rem;">Ім'я Прізвище</p>
  <p style="margin: 0.25rem 0 0 0; color: #58595b; font-size: 0.875rem;">Посада</p>
  <p style="margin: 0.25rem 0 0 0; color: #9d9fa2; font-size: 0.875rem;">Факультет прикладних наук УКУ</p>
  
  <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #e5e7eb;">
    <p style="margin: 0; color: #58595b; font-size: 0.8rem;">
      <strong>Тел.:</strong> +380 32 240 99 44<br>
      <strong>Email:</strong> email@ucu.edu.ua<br>
      <strong>Web:</strong> <a href="https://apps.ucu.edu.ua" style="color: #662d91;">apps.ucu.edu.ua</a>
    </p>
  </div>
  
  <div style="margin-top: 1rem;">
    <img src="../../assets/logo/logo_aps_eng_full_color.svg" alt="APPS Logo" style="height: 40px;">
  </div>
</div>

---

## Структура підпису

```
Ім'я Прізвище
Посада
Факультет прикладних наук УКУ

Тел.: +380 32 240 99 44
Email: email@ucu.edu.ua
Web: apps.ucu.edu.ua

[Логотип]
```

---

## Варіанти підписів

### Базовий (без логотипу)

<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; margin: 1rem 0; font-family: Arial, sans-serif;">
  <p style="margin: 0; color: #662d91; font-weight: 600;">Ім'я Прізвище</p>
  <p style="margin: 0.25rem 0 0 0; color: #58595b; font-size: 0.9rem;">Посада | Факультет прикладних наук УКУ</p>
  <p style="margin: 0.5rem 0 0 0; color: #9d9fa2; font-size: 0.85rem;">+380 32 240 99 44 | apps.ucu.edu.ua</p>
</div>

### Розширений (з соціальними мережами)

<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; margin: 1rem 0; font-family: Arial, sans-serif;">
  <div style="display: flex; gap: 1rem; align-items: flex-start;">
    <img src="../../assets/logo/logo_aps_eng_full_color.svg" alt="APPS Logo" style="height: 50px;">
    <div>
      <p style="margin: 0; color: #662d91; font-weight: 600;">Ім'я Прізвище</p>
      <p style="margin: 0.25rem 0 0 0; color: #58595b; font-size: 0.9rem;">Посада</p>
      <p style="margin: 0.25rem 0 0 0; color: #9d9fa2; font-size: 0.85rem;">Факультет прикладних наук УКУ</p>
      <p style="margin: 0.5rem 0 0 0; color: #58595b; font-size: 0.85rem;">
        +380 32 240 99 44 | apps.ucu.edu.ua
      </p>
      <p style="margin: 0.5rem 0 0 0; font-size: 0.85rem;">
        <a href="#" style="color: #662d91; text-decoration: none; margin-right: 0.5rem;">LinkedIn</a>
        <a href="#" style="color: #662d91; text-decoration: none;">Instagram</a>
      </p>
    </div>
  </div>
</div>

---

## Специфікації

### Типографіка

| Елемент | Шрифт | Розмір | Колір |
|---------|-------|--------|-------|
| **Ім'я** | Arial Bold | 12 pt | #662d91 |
| **Посада** | Arial Regular | 11 pt | #58595b |
| **Організація** | Arial Regular | 11 pt | #9d9fa2 |
| **Контакти** | Arial Regular | 10 pt | #58595b |

### Розміри

| Елемент | Значення |
|---------|----------|
| **Логотип** | Висота 40-50 px |
| **Загальна ширина** | Макс. 400 px |
| **Відступи** | 10-15 px |

---

## HTML-код підпису

=== "Стандартний"

    ```html
    <table cellpadding="0" cellspacing="0" style="font-family: Arial, sans-serif;">
      <tr>
        <td style="border-left: 3px solid #662d91; padding-left: 15px;">
          <p style="margin: 0; font-weight: bold; color: #662d91; font-size: 14px;">
            Ім'я Прізвище
          </p>
          <p style="margin: 2px 0 0 0; color: #58595b; font-size: 13px;">
            Посада
          </p>
          <p style="margin: 2px 0 0 0; color: #9d9fa2; font-size: 13px;">
            Факультет прикладних наук УКУ
          </p>
          <p style="margin: 10px 0 0 0; color: #58595b; font-size: 12px;">
            Тел.: +380 32 240 99 44<br>
            Email: email@ucu.edu.ua<br>
            Web: <a href="https://apps.ucu.edu.ua" style="color: #662d91;">apps.ucu.edu.ua</a>
          </p>
        </td>
      </tr>
    </table>
    ```

=== "З логотипом"

    ```html
    <table cellpadding="0" cellspacing="0" style="font-family: Arial, sans-serif;">
      <tr>
        <td style="padding-right: 15px; vertical-align: top;">
          <img src="logo_url" alt="APPS UCU" style="height: 50px;">
        </td>
        <td style="border-left: 2px solid #662d91; padding-left: 15px;">
          <p style="margin: 0; font-weight: bold; color: #662d91; font-size: 14px;">
            Ім'я Прізвище
          </p>
          <p style="margin: 2px 0 0 0; color: #58595b; font-size: 13px;">
            Посада | Факультет прикладних наук УКУ
          </p>
          <p style="margin: 8px 0 0 0; color: #58595b; font-size: 12px;">
            +380 32 240 99 44 | apps.ucu.edu.ua
          </p>
        </td>
      </tr>
    </table>
    ```

---

## Налаштування

### Gmail

1. Відкрийте **Налаштування** → **Загальні**
2. Прокрутіть до **Підпис**
3. Вставте HTML-код або відформатований текст
4. Збережіть зміни

### Outlook

1. **Файл** → **Параметри** → **Пошта** → **Підписи**
2. Створіть новий підпис
3. Вставте HTML-код
4. Встановіть як підпис за замовчуванням

---

## Правила використання

!!! success "Рекомендовано"
    - Використовуйте стандартний формат для всіх співробітників
    - Оновлюйте контактну інформацію при зміні посади
    - Використовуйте офіційну email-адресу @ucu.edu.ua

!!! warning "Уникайте"
    - Додавання цитат або мотиваційних фраз
    - Використання нестандартних шрифтів
    - Додавання великих зображень
    - Анімованих GIF-файлів

[:fontawesome-solid-arrow-left: Повернутися до шаблонів](index.md){ .md-button }
