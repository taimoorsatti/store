import os
import json
import zipfile

BASE_DIR = '/app/applet/shopify-theme'

def write(rel_path, content):
    full_path = os.path.join(BASE_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

print("Generating Shopify Online Store 2.0 Theme files for FABFaddons...")

# 1. config/settings_schema.json
write('config/settings_schema.json', '''[
  {
    "name": "theme_info",
    "theme_name": "FABFaddons Luxury OS 2.0",
    "theme_version": "1.0.0",
    "theme_author": "FABFaddons UAE Agency",
    "theme_documentation_url": "https://fabfaddons.com/docs",
    "theme_support_url": "https://fabfaddons.com/support"
  },
  {
    "name": "t:settings_schema.colors.name",
    "settings": [
      {
        "type": "color",
        "id": "color_primary",
        "label": "Primary Brand Color (Deep Burgundy)",
        "default": "#351C27"
      },
      {
        "type": "color",
        "id": "color_background",
        "label": "Primary Background (Warm Ivory)",
        "default": "#F7F3ED"
      },
      {
        "type": "color",
        "id": "color_accent",
        "label": "Luxury Accent (Champagne Gold)",
        "default": "#C5A477"
      },
      {
        "type": "color",
        "id": "color_secondary_bg",
        "label": "Secondary Background (Warm Beige)",
        "default": "#E9DFD5"
      },
      {
        "type": "color",
        "id": "color_text_primary",
        "label": "Primary Text (Rich Charcoal)",
        "default": "#29231F"
      },
      {
        "type": "color",
        "id": "color_text_muted",
        "label": "Secondary Muted Text",
        "default": "#766B64"
      }
    ]
  },
  {
    "name": "t:settings_schema.typography.name",
    "settings": [
      {
        "type": "font_picker",
        "id": "font_heading",
        "label": "Heading Font (Luxury Serif)",
        "default": "playfair_display_n7"
      },
      {
        "type": "font_picker",
        "id": "font_body",
        "label": "Body Font",
        "default": "assistant_n4"
      }
    ]
  },
  {
    "name": "UAE & Dropshipping Settings",
    "settings": [
      {
        "type": "text",
        "id": "currency_code",
        "label": "Primary Currency",
        "default": "AED"
      },
      {
        "type": "number",
        "id": "free_shipping_threshold",
        "label": "Free UAE Delivery Threshold (AED)",
        "default": 250
      },
      {
        "type": "checkbox",
        "id": "enable_cod_badge",
        "label": "Display Cash on Delivery (COD) badge",
        "default": true
      },
      {
        "type": "text",
        "id": "concierge_whatsapp",
        "label": "UAE WhatsApp Concierge (+971)",
        "default": "+971501234567"
      }
    ]
  }
]''')

# 2. config/settings_data.json
write('config/settings_data.json', '''{
  "current": {
    "color_primary": "#351C27",
    "color_background": "#F7F3ED",
    "color_accent": "#C5A477",
    "color_secondary_bg": "#E9DFD5",
    "color_text_primary": "#29231F",
    "color_text_muted": "#766B64",
    "currency_code": "AED",
    "free_shipping_threshold": 250,
    "enable_cod_badge": true,
    "concierge_whatsapp": "+971501234567",
    "sections": {
      "announcement-bar": {
        "type": "announcement-bar",
        "settings": {
          "text": "Complimentary UAE Express Delivery on Orders Over AED 250 · 100% Authentic Beauty Essentials",
          "enable_language_selector": true
        }
      },
      "header": {
        "type": "header",
        "settings": {
          "logo_text": "FABFaddons",
          "enable_sticky": true
        }
      },
      "footer": {
        "type": "footer",
        "settings": {}
      }
    }
  }
}''')

# 3. locales/en.default.json
write('locales/en.default.json', '''{
  "general": {
    "meta": {
      "tags": "Tagged \\"{{ tags }}\\"",
      "page": "Page {{ page }}"
    },
    "404": {
      "title": "404 - Page Not Found",
      "subtext": "The beauty ritual page you are searching for is unavailable.",
      "link": "Return to Storefront"
    },
    "password_page": {
      "login_form_heading": "Enter store using password",
      "login_form_password_label": "Password",
      "login_form_password_placeholder": "Your password",
      "login_form_submit": "Enter"
    },
    "continue_shopping": "Continue Shopping",
    "search": {
      "search": "Search beauty essentials...",
      "submit": "Search",
      "heading": "Search Results for \\"{{ terms }}\\"",
      "no_results": "No beauty rituals matched your query."
    }
  },
  "accessibility": {
    "skip_to_text": "Skip to content",
    "close": "Close",
    "unit_price_separator": "per"
  },
  "sections": {
    "header": {
      "menu": "Menu",
      "cart_count": {
        "one": "{{ count }} item",
        "other": "{{ count }} items"
      }
    },
    "cart": {
      "title": "Your Shopping Bag",
      "empty": "Your bag is empty",
      "subtotal": "Subtotal",
      "checkout": "Proceed to Checkout",
      "free_shipping_unlocked": "Complimentary UAE Delivery Unlocked!",
      "free_shipping_away": "Add {{ amount }} more for Free UAE Delivery"
    },
    "featured_products": {
      "title": "The Launch Collection",
      "subtitle": "Carefully selected luxury beauty & skincare devices",
      "view_all": "View All Products"
    }
  },
  "products": {
    "product": {
      "add_to_cart": "Add to Bag",
      "sold_out": "Sold Out",
      "unavailable": "Unavailable",
      "on_sale": "Save",
      "quantity": {
        "label": "Quantity",
        "input_label": "Quantity for {{ product }}",
        "increase": "Increase quantity for {{ product }}",
        "decrease": "Decrease quantity for {{ product }}"
      },
      "uae_delivery": "UAE Express Delivery in 1–2 business days",
      "cod_available": "Cash on Delivery (COD) & Apple Pay supported"
    }
  },
  "settings_schema": {
    "colors": {
      "name": "Luxury Colors"
    },
    "typography": {
      "name": "Typography"
    }
  }
}''')

# 4. locales/ar.json
write('locales/ar.json', '''{
  "general": {
    "404": {
      "title": "404 - الصفحة غير موجودة",
      "subtext": "الصفحة التي تبحثين عنها غير متوفرة حالياً.",
      "link": "العودة للمتجر"
    },
    "continue_shopping": "متابعة التسوق",
    "search": {
      "search": "ابحثي عن أدوات التجميل والسيروم...",
      "submit": "بحث",
      "heading": "نتائج البحث عن \\"{{ terms }}\\"",
      "no_results": "لم نجد نتائج مطابقة لبحثك."
    }
  },
  "sections": {
    "header": {
      "menu": "القائمة"
    },
    "cart": {
      "title": "حقيبة التسوق",
      "empty": "حقيبة التسوق فارغة",
      "subtotal": "المجموع الفرعي",
      "checkout": "إتمام الطلب بأمان",
      "free_shipping_unlocked": "مبروك! حصلتِ على توصيل سريع مجاني في الإمارات",
      "free_shipping_away": "أضيفي منتجات بقيمة {{ amount }} درهم للشحن المجاني"
    },
    "featured_products": {
      "title": "المجموعة الافتتاحية الحصرية",
      "subtitle": "أجهزة ومستحضرات تجميل مختارة بعناية للمرأة العصرية",
      "view_all": "عرض جميع المنتجات"
    }
  },
  "products": {
    "product": {
      "add_to_cart": "إضافة إلى الحقيبة",
      "sold_out": "نفدت الكمية",
      "unavailable": "غير متوفر",
      "on_sale": "خصم",
      "uae_delivery": "توصيل سريع بالإمارات خلال 1-2 يوم عمل",
      "cod_available": "الدفع عند الاستلام وآبل باي متوفران"
    }
  }
}''')

# 5. layout/theme.liquid
write('layout/theme.liquid', '''<!doctype html>
<html class="no-js" lang="{{ request.locale.iso_code }}" dir="{% if request.locale.iso_code == 'ar' %}rtl{% else %}ltr{% endif %}">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, height=device-height, minimum-scale=1.0">
    <link rel="canonical" href="{{ canonical_url }}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">

    {%- if settings.favicon != blank -%}
      <link rel="icon" type="image/png" href="{{ settings.favicon | image_url: width: 32, height: 32 }}">
    {%- endif -%}

    <title>
      {{ page_title }}
      {%- if current_tags %} &ndash; tagged "{{ current_tags | join: ', ' }}"{% endif -%}
      {%- if current_page != 1 %} &ndash; Page {{ current_page }}{% endif -%}
      {%- unless page_title contains shop.name %} &ndash; {{ shop.name }}{% endunless -%}
    </title>

    {% if page_description %}
      <meta name="description" content="{{ page_description | escape }}">
    {% endif %}

    {% render 'meta-tags' %}

    {{ content_for_header }}

    <style>
      :root {
        --color-primary: {{ settings.color_primary | default: '#351C27' }};
        --color-bg: {{ settings.color_background | default: '#F7F3ED' }};
        --color-accent: {{ settings.color_accent | default: '#C5A477' }};
        --color-secondary-bg: {{ settings.color_secondary_bg | default: '#E9DFD5' }};
        --color-text: {{ settings.color_text_primary | default: '#29231F' }};
        --color-text-muted: {{ settings.color_text_muted | default: '#766B64' }};
        --font-heading: 'Playfair Display', Georgia, serif;
        --font-body: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      }
      [dir="rtl"] {
        --font-body: 'Tajawal', system-ui, sans-serif;
        --font-heading: 'Tajawal', Georgia, serif;
      }
    </style>

    {{ 'theme.css' | asset_url | stylesheet_tag }}
    <script src="{{ 'theme.js' | asset_url }}" defer="defer"></script>
  </head>

  <body class="template-{{ template.name | handle }} bg-ivory text-charcoal antialiased">
    <a class="skip-to-content-link button visually-hidden" href="#MainContent">
      {{ "accessibility.skip_to_text" | t }}
    </a>

    {% section 'announcement-bar' %}
    {% section 'header' %}

    <main id="MainContent" class="content-for-layout focus-none" role="main" tabindex="-1">
      {{ content_for_layout }}
    </main>

    {% section 'footer' %}

    {% render 'cart-drawer' %}

    <script>
      window.shopUrl = '{{ request.origin }}';
      window.routes = {
        cart_add_url: '{{ routes.cart_add_url }}',
        cart_change_url: '{{ routes.cart_change_url }}',
        cart_update_url: '{{ routes.cart_update_url }}',
        cart_url: '{{ routes.cart_url }}',
        predictive_search_url: '{{ routes.predictive_search_url }}'
      };
      window.cartStrings = {
        error: `{{ 'sections.cart.cart_error' | t }}`,
        quantityError: `{{ 'sections.cart.cart_quantity_error_html' | t: quantity: '[quantity]' }}`
      };
    </script>
  </body>
</html>''')

# 6. layout/password.liquid
write('layout/password.liquid', '''<!doctype html>
<html class="no-js" lang="{{ request.locale.iso_code }}">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ shop.name }} &ndash; Opening Soon</title>
    {{ content_for_header }}
    {{ 'theme.css' | asset_url | stylesheet_tag }}
  </head>
  <body class="bg-ivory text-charcoal flex items-center justify-center min-h-screen p-6 text-center">
    <div class="max-w-md w-full p-8 bg-white rounded-xl shadow-lg border border-[#E9DFD5]">
      <h1 class="text-3xl font-serif text-[#351C27] font-bold mb-2">FABFaddons</h1>
      <p class="text-sm text-[#766B64] mb-6">Beauty. Confidence. You. Opening in the UAE soon.</p>
      {{ content_for_layout }}
    </div>
  </body>
</html>''')

# 7. assets/theme.css
write('assets/theme.css', '''/* FABFaddons Shopify OS 2.0 Luxury Stylesheet */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: var(--font-body);
  background-color: var(--color-bg);
  color: var(--color-text);
  line-height: 1.6;
}

h1, h2, h3, h4, .font-serif {
  font-family: var(--font-heading);
  letter-spacing: -0.015em;
  color: var(--color-primary);
}

a {
  color: inherit;
  text-decoration: none;
}

button {
  font-family: inherit;
  cursor: pointer;
  border: none;
  background: none;
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}

.visually-hidden {
  position: absolute !important;
  overflow: hidden;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  border: 0;
  clip: rect(0 0 0 0);
  word-wrap: normal !important;
}

/* Container */
.container {
  max-width: 1280px;
  margin-left: auto;
  margin-right: auto;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
}

/* Luxury Buttons */
.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  background-color: var(--color-primary);
  color: var(--color-bg);
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 0.875rem 2rem;
  border-radius: 2px;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}
.btn-primary:hover {
  background-color: #201117;
  color: #FFFFFF;
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  border: 1px solid var(--color-primary);
  color: var(--color-primary);
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 0.875rem 2rem;
  border-radius: 2px;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}
.btn-secondary:hover {
  background-color: var(--color-secondary-bg);
}

/* Product Card Grid */
.product-grid {
  display: grid;
  grid-template-columns: repeat(1, minmax(0, 1fr));
  gap: 1.5rem;
}
@media (min-width: 640px) {
  .product-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
@media (min-width: 1024px) {
  .product-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

.product-card {
  background: #FFFFFF;
  border: 1px solid var(--color-secondary-bg);
  border-radius: 12px;
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
}
.product-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px -5px rgba(53, 28, 39, 0.08);
}
.product-card__image-wrapper {
  position: relative;
  aspect-ratio: 4/3;
  background-color: rgba(233, 223, 213, 0.4);
  overflow: hidden;
}
.product-card__image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}
.product-card:hover .product-card__image {
  transform: scale(1.04);
}
.product-card__content {
  padding: 1.25rem;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

/* Cart Drawer */
.cart-drawer-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.45);
  backdrop-filter: blur(2px);
  z-index: 100;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
}
.cart-drawer-overlay.active {
  opacity: 1;
  pointer-events: auto;
}
.cart-drawer {
  position: fixed;
  top: 0;
  bottom: 0;
  right: 0;
  width: 100%;
  max-width: 440px;
  background: var(--color-bg);
  z-index: 101;
  transform: translateX(100%);
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
  box-shadow: -10px 0 30px rgba(0,0,0,0.15);
}
[dir="rtl"] .cart-drawer {
  right: auto;
  left: 0;
  transform: translateX(-100%);
}
.cart-drawer.active {
  transform: translateX(0);
}
''')

# 8. assets/theme.js
write('assets/theme.js', '''// FABFaddons Theme JavaScript (Shopify OS 2.0 native Ajax Cart & UI)
document.addEventListener('DOMContentLoaded', () => {
  // Cart Drawer open/close
  const cartTrigger = document.querySelector('[data-cart-drawer-trigger]');
  const cartDrawer = document.querySelector('#cart-drawer');
  const cartOverlay = document.querySelector('#cart-drawer-overlay');
  const cartClose = document.querySelector('[data-cart-drawer-close]');

  function openCart() {
    if (cartDrawer) cartDrawer.classList.add('active');
    if (cartOverlay) cartOverlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeCart() {
    if (cartDrawer) cartDrawer.classList.remove('active');
    if (cartOverlay) cartOverlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (cartTrigger) cartTrigger.addEventListener('click', openCart);
  if (cartClose) cartClose.addEventListener('click', closeCart);
  if (cartOverlay) cartOverlay.addEventListener('click', closeCart);

  // Quick Ajax Add To Cart
  document.querySelectorAll('form[action*="/cart/add"]').forEach(form => {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const formData = new FormData(form);
      try {
        const res = await fetch('/cart/add.js', {
          method: 'POST',
          body: formData
        });
        if (res.ok) {
          // Refresh cart drawer or redirect
          openCart();
          fetchCart();
        }
      } catch (err) {
        console.error('Add to cart failed', err);
        form.submit();
      }
    });
  });

  async function fetchCart() {
    try {
      const res = await fetch('/cart.js');
      const cart = await res.json();
      const badge = document.querySelector('[data-cart-count-badge]');
      if (badge) {
        badge.textContent = cart.item_count;
        badge.style.display = cart.item_count > 0 ? 'inline-flex' : 'none';
      }
    } catch (e) {
      // quiet
    }
  }
});
''')

# 9. snippets/product-card.liquid
write('snippets/product-card.liquid', '''{% comment %}
  Renders a luxury product card
  Accepts: product {Object}
{% endcomment %}
<div class="product-card group">
  <div class="product-card__image-wrapper">
    <a href="{{ product.url }}">
      {%- if product.featured_media -%}
        {{ product.featured_media | image_url: width: 600 | image_tag: loading: 'lazy', class: 'product-card__image', alt: product.title }}
      {%- else -%}
        {{ 'product-1' | placeholder_svg_tag }}
      {%- endif -%}
    </a>
    {%- if product.compare_at_price > product.price -%}
      <div style="position: absolute; top: 12px; right: 12px; background: #E9DFD5; color: #351C27; font-size: 11px; font-weight: bold; padding: 2px 8px; border-radius: 3px;">
        -{{ product.compare_at_price | minus: product.price | times: 100.0 | divided_by: product.compare_at_price | round }}%
      </div>
    {%- endif -%}
  </div>

  <div class="product-card__content">
    <div>
      <div style="font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--color-accent); margin-bottom: 4px; font-weight: 600;">
        {{ product.type | default: 'Luxury Beauty' }}
      </div>
      <h3 style="font-size: 1.05rem; font-weight: 600; line-height: 1.3; margin-bottom: 6px;">
        <a href="{{ product.url }}">{{ product.title }}</a>
      </h3>
    </div>

    <div style="margin-top: 14px; padding-top: 10px; border-top: 1px solid rgba(233, 223, 213, 0.8); display: flex; align-items: center; justify-content: space-between;">
      <div>
        <span style="font-weight: 700; color: var(--color-primary); font-size: 1.05rem;">
          {{ product.price | money }}
        </span>
        {%- if product.compare_at_price > product.price -%}
          <span style="font-size: 0.85rem; color: var(--color-text-muted); text-decoration: line-through; margin-left: 6px;">
            {{ product.compare_at_price | money }}
          </span>
        {%- endif -%}
      </div>

      <form method="post" action="/cart/add">
        <input type="hidden" name="id" value="{{ product.selected_or_first_available_variant.id }}">
        <button type="submit" class="btn-primary" style="padding: 0.5rem 1rem; font-size: 11px;">
          {{ 'products.product.add_to_cart' | t }}
        </button>
      </form>
    </div>
  </div>
</div>''')

# 10. snippets/cart-drawer.liquid
write('snippets/cart-drawer.liquid', '''<div id="cart-drawer-overlay" class="cart-drawer-overlay"></div>
<aside id="cart-drawer" class="cart-drawer" role="dialog" aria-modal="true" aria-label="{{ 'sections.cart.title' | t }}">
  <div style="padding: 1.25rem 1.5rem; border-bottom: 1px solid var(--color-secondary-bg); display: flex; align-items: center; justify-content: space-between;">
    <h2 style="font-size: 1.25rem; font-weight: 700;">{{ 'sections.cart.title' | t }}</h2>
    <button data-cart-drawer-close aria-label="Close cart" style="font-size: 1.25rem; color: var(--color-text-muted);">&times;</button>
  </div>

  <div style="flex: 1; overflow-y: auto; padding: 1.5rem;">
    {%- if cart.item_count == 0 -%}
      <div style="text-align: center; padding: 3rem 1rem;">
        <p style="color: var(--color-text-muted); font-size: 0.95rem; margin-bottom: 1.5rem;">{{ 'sections.cart.empty' | t }}</p>
        <a href="{{ routes.all_products_collection_url }}" class="btn-primary">{{ 'general.continue_shopping' | t }}</a>
      </div>
    {%- else -%}
      <ul style="list-style: none; display: flex; flex-direction: column; gap: 1rem;">
        {%- for item in cart.items -%}
          <li style="display: flex; gap: 1rem; border-bottom: 1px solid var(--color-secondary-bg); padding-bottom: 1rem;">
            {%- if item.image -%}
              <img src="{{ item.image | image_url: width: 120 }}" alt="{{ item.title }}" style="width: 70px; height: 70px; object-fit: cover; border-radius: 6px;">
            {%- endif -%}
            <div style="flex: 1;">
              <h4 style="font-size: 0.95rem; font-weight: 600;"><a href="{{ item.url }}">{{ item.product.title }}</a></h4>
              <p style="font-size: 0.8rem; color: var(--color-text-muted);">{{ item.variant.title }}</p>
              <div style="margin-top: 6px; display: flex; justify-content: space-between; align-items: center;">
                <span style="font-size: 0.85rem;">Qty: {{ item.quantity }}</span>
                <span style="font-weight: 700; color: var(--color-primary);">{{ item.final_line_price | money }}</span>
              </div>
            </div>
          </li>
        {%- endfor -%}
      </ul>
    {%- endif -%}
  </div>

  {%- if cart.item_count > 0 -%}
    <div style="padding: 1.5rem; border-top: 1px solid var(--color-secondary-bg); background: #FFFFFF;">
      <div style="display: flex; justify-content: space-between; font-size: 1.05rem; font-weight: 700; margin-bottom: 1rem;">
        <span>{{ 'sections.cart.subtotal' | t }}</span>
        <span>{{ cart.total_price | money }}</span>
      </div>
      <a href="/checkout" class="btn-primary" style="width: 100%;">{{ 'sections.cart.checkout' | t }}</a>
    </div>
  {%- endif -%}
</aside>''')

# 11. snippets/meta-tags.liquid
write('snippets/meta-tags.liquid', '''<meta property="og:site_name" content="{{ shop.name }}">
<meta property="og:url" content="{{ canonical_url }}">
<meta property="og:title" content="{{ page_title | default: shop.name }}">
<meta property="og:type" content="website">
<meta property="og:description" content="{{ page_description | default: shop.description }}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{{ page_title | default: shop.name }}">
<meta name="twitter:description" content="{{ page_description | default: shop.description }}">''')

# 12. sections/announcement-bar.liquid
write('sections/announcement-bar.liquid', '''{%- if section.settings.show_announcement -%}
  <div style="background-color: var(--color-primary); color: #F7F3ED; padding: 0.5rem 1rem; font-size: 0.75rem; font-weight: 500; text-align: center; letter-spacing: 0.05em;">
    <div class="container" style="display: flex; justify-content: space-between; align-items: center;">
      <span style="color: var(--color-accent); font-size: 0.7rem; text-transform: uppercase;">UAE Free Express Delivery</span>
      <span>{{ section.settings.text }}</span>
      <span style="font-size: 0.7rem; opacity: 0.8;">100% Authentic</span>
    </div>
  </div>
{%- endif -%}

{% schema %}
{
  "name": "Announcement Bar",
  "settings": [
    {
      "type": "checkbox",
      "id": "show_announcement",
      "label": "Show announcement",
      "default": true
    },
    {
      "type": "text",
      "id": "text",
      "label": "Announcement text",
      "default": "Complimentary UAE Express Delivery on Orders Over AED 250 · 100% Authentic Beauty Essentials"
    }
  ]
}
{% endschema %}''')

# 13. sections/header.liquid
write('sections/header.liquid', '''<header style="background: var(--color-bg); border-bottom: 1px solid var(--color-secondary-bg); position: sticky; top: 0; z-index: 50;">
  <div class="container" style="height: 5rem; display: flex; align-items: center; justify-content: space-between; gap: 2rem;">
    <!-- Brand Wordmark -->
    <a href="{{ routes.root_url }}" style="display: flex; flex-direction: column;">
      <span style="font-family: var(--font-heading); font-size: 1.75rem; font-weight: 700; color: var(--color-primary); letter-spacing: -0.02em;">
        {{ section.settings.logo_text | default: shop.name }}
      </span>
      <span style="font-size: 9px; letter-spacing: 0.25em; text-transform: uppercase; color: var(--color-text-muted);">
        DUBAI · HAUTE BEAUTÉ
      </span>
    </a>

    <!-- Navigation links -->
    <nav style="display: flex; gap: 1.75rem; font-size: 0.8125rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">
      {%- for link in linklists.main-menu.links -%}
        <a href="{{ link.url }}" style="color: var(--color-text); transition: color 0.2s;">
          {{ link.title }}
        </a>
      {%- else -%}
        <a href="{{ routes.root_url }}">Home</a>
        <a href="{{ routes.all_products_collection_url }}">Shop All</a>
        <a href="/pages/about">About Us</a>
        <a href="/pages/contact">Contact</a>
      {%- endfor -%}
    </nav>

    <!-- Affordances -->
    <div style="display: flex; align-items: center; gap: 1rem;">
      <a href="{{ routes.search_url }}" aria-label="Search" style="padding: 0.5rem; color: var(--color-text);">
        <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
      </a>

      <button data-cart-drawer-trigger aria-label="Open Cart" style="position: relative; padding: 0.5rem; color: var(--color-primary); display: flex; align-items: center;">
        <svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
        <span data-cart-count-badge style="position: absolute; top: 0; right: 0; background: var(--color-primary); color: #FFF; font-size: 10px; font-weight: 700; width: 18px; height: 18px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
          {{ cart.item_count }}
        </span>
      </button>
    </div>
  </div>
</header>

{% schema %}
{
  "name": "Header",
  "settings": [
    {
      "type": "text",
      "id": "logo_text",
      "label": "Logo text",
      "default": "FABFaddons"
    }
  ]
}
{% endschema %}''')

# 14. sections/hero-banner.liquid
write('sections/hero-banner.liquid', '''<section style="background: var(--color-bg); padding: 4rem 0; border-bottom: 1px solid var(--color-secondary-bg);">
  <div class="container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 3rem; align-items: center;">
    <div>
      <span style="color: var(--color-accent); font-size: 0.75rem; letter-spacing: 0.15em; text-transform: uppercase; font-weight: 700; display: block; margin-bottom: 1rem;">
        {{ section.settings.subheading }}
      </span>
      <h1 style="font-size: 3.25rem; font-weight: 700; line-height: 1.15; margin-bottom: 1.25rem; color: var(--color-primary);">
        {{ section.settings.heading }}
      </h1>
      <p style="font-size: 1.125rem; color: var(--color-text-muted); margin-bottom: 2rem; max-width: 500px;">
        {{ section.settings.text }}
      </p>
      <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
        <a href="{{ section.settings.button_link | default: routes.all_products_collection_url }}" class="btn-primary">
          {{ section.settings.button_label }}
        </a>
        <a href="/collections/tools" class="btn-secondary">
          Explore Collection
        </a>
      </div>
    </div>

    <div>
      {%- if section.settings.image != blank -%}
        {{ section.settings.image | image_url: width: 1000 | image_tag: loading: 'eager', style: 'border-radius: 12px; width: 100%; height: auto; box-shadow: 0 20px 40px rgba(0,0,0,0.1);' }}
      {%- else -%}
        <div style="aspect-ratio: 4/3; background: var(--color-secondary-bg); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: var(--color-text-muted); font-family: var(--font-heading); font-size: 1.5rem;">
          FABFaddons Luxury Editorial
        </div>
      {%- endif -%}
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Hero Banner",
  "settings": [
    {
      "type": "text",
      "id": "subheading",
      "label": "Subheading",
      "default": "HAUTE LUXURY BEAUTY · UAE EDITION"
    },
    {
      "type": "text",
      "id": "heading",
      "label": "Heading",
      "default": "Discover Your Everyday Beauty Ritual."
    },
    {
      "type": "textarea",
      "id": "text",
      "label": "Text",
      "default": "Explore carefully selected beauty and skincare essentials designed to elevate your everyday routine."
    },
    {
      "type": "text",
      "id": "button_label",
      "label": "Primary Button Label",
      "default": "SHOP NOW"
    },
    {
      "type": "url",
      "id": "button_link",
      "label": "Primary Button Link"
    },
    {
      "type": "image_picker",
      "id": "image",
      "label": "Campaign Image"
    }
  ],
  "presets": [
    {
      "name": "Hero Banner"
    }
  ]
}
{% endschema %}''')

# 15. sections/featured-products.liquid
write('sections/featured-products.liquid', '''<section style="padding: 5rem 0; background: var(--color-bg);">
  <div class="container">
    <div style="text-align: center; margin-bottom: 3.5rem;">
      <h2 style="font-size: 2.25rem; font-weight: 700; margin-bottom: 0.5rem;">
        {{ section.settings.title | default: 'The Launch Collection' }}
      </h2>
      <p style="color: var(--color-text-muted); font-size: 1rem; max-width: 600px; margin: 0 auto;">
        {{ section.settings.subtitle | default: 'Six meticulously engineered beauty essentials, crafted for modern luxury living.' }}
      </p>
    </div>

    <div class="product-grid">
      {%- assign collection = collections[section.settings.collection] -%}
      {%- for product in collection.products limit: section.settings.products_to_show -%}
        {% render 'product-card', product: product %}
      {%- else -%}
        {%- for i in (1..6) -%}
          <div class="product-card" style="padding: 2rem; text-align: center;">
            <p style="font-family: var(--font-heading); font-size: 1.1rem; margin-bottom: 0.5rem;">Launch Beauty Essential {{ i }}</p>
            <p style="color: var(--color-primary); font-weight: 700;">AED 249</p>
          </div>
        {%- endfor -%}
      {%- endfor -%}
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Featured Products",
  "settings": [
    {
      "type": "text",
      "id": "title",
      "label": "Heading",
      "default": "The Launch Collection"
    },
    {
      "type": "text",
      "id": "subtitle",
      "label": "Subtitle",
      "default": "Six meticulously engineered beauty essentials, crafted for modern luxury living."
    },
    {
      "type": "collection",
      "id": "collection",
      "label": "Collection"
    },
    {
      "type": "range",
      "id": "products_to_show",
      "min": 2,
      "max": 12,
      "step": 1,
      "default": 6,
      "label": "Number of products"
    }
  ],
  "presets": [
    {
      "name": "Featured Products"
    }
  ]
}
{% endschema %}''')

# 16. sections/promotional-banner.liquid
write('sections/promotional-banner.liquid', '''<section style="background-color: var(--color-primary); color: #F7F3ED; padding: 5rem 0; margin: 2rem 0;">
  <div class="container" style="text-align: center; max-width: 760px;">
    <span style="color: var(--color-accent); font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase; font-weight: 700; display: block; margin-bottom: 1rem;">
      Editorial Showcase
    </span>
    <h2 style="color: #F7F3ED; font-size: 2.75rem; line-height: 1.2; margin-bottom: 1.25rem;">
      {{ section.settings.heading }}
    </h2>
    <p style="color: rgba(247, 243, 237, 0.8); font-size: 1.125rem; margin-bottom: 2rem;">
      {{ section.settings.text }}
    </p>
    <a href="{{ section.settings.button_link | default: routes.all_products_collection_url }}" class="btn-primary" style="background-color: var(--color-accent); color: var(--color-primary);">
      {{ section.settings.button_label }}
    </a>
  </div>
</section>

{% schema %}
{
  "name": "Promotional Banner",
  "settings": [
    {
      "type": "text",
      "id": "heading",
      "label": "Headline",
      "default": "Your Beauty. Your Everyday Luxury."
    },
    {
      "type": "textarea",
      "id": "text",
      "label": "Supporting text",
      "default": "Explore beauty essentials selected to complement your everyday routine."
    },
    {
      "type": "text",
      "id": "button_label",
      "label": "CTA Button",
      "default": "EXPLORE NOW"
    },
    {
      "type": "url",
      "id": "button_link",
      "label": "CTA Link"
    }
  ],
  "presets": [
    {
      "name": "Promotional Banner"
    }
  ]
}
{% endschema %}''')

# 17. sections/why-choose-us.liquid
write('sections/why-choose-us.liquid', '''<section style="padding: 5rem 0; background: var(--color-secondary-bg); border-top: 1px solid rgba(0,0,0,0.05); border-bottom: 1px solid rgba(0,0,0,0.05);">
  <div class="container">
    <div style="text-align: center; margin-bottom: 3.5rem;">
      <h2 style="font-size: 2.25rem; font-weight: 700; margin-bottom: 0.5rem;">
        {{ section.settings.heading | default: 'Why Choose FABFaddons?' }}
      </h2>
      <p style="color: var(--color-text-muted); font-size: 1rem;">
        An unwavering commitment to curated beauty, transparency, and rapid regional fulfillment.
      </p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 2rem;">
      <div style="background: #FFFFFF; padding: 2.25rem; border-radius: 12px; border: 1px solid rgba(233, 223, 213, 0.8);">
        <h3 style="font-size: 1.15rem; font-weight: 700; margin-bottom: 0.75rem;">1. Carefully Selected Beauty Essentials</h3>
        <p style="color: var(--color-text-muted); font-size: 0.875rem;">Strict quality criteria, dermatologist-tested formulas, and ergonomic tools chosen specifically for UAE skin and climate.</p>
      </div>

      <div style="background: #FFFFFF; padding: 2.25rem; border-radius: 12px; border: 1px solid rgba(233, 223, 213, 0.8);">
        <h3 style="font-size: 1.15rem; font-weight: 700; margin-bottom: 0.75rem;">2. Convenient Shopping Experience</h3>
        <p style="color: var(--color-text-muted); font-size: 0.875rem;">Fast 24–48 hour dispatch across Dubai, Abu Dhabi and the Emirates with real-time SMS and email tracking.</p>
      </div>

      <div style="background: #FFFFFF; padding: 2.25rem; border-radius: 12px; border: 1px solid rgba(233, 223, 213, 0.8);">
        <h3 style="font-size: 1.15rem; font-weight: 700; margin-bottom: 0.75rem;">3. Secure Payment Options</h3>
        <p style="color: var(--color-text-muted); font-size: 0.875rem;">Pay securely via Visa, Mastercard, Apple Pay, Tabby/Tamara installments, or Cash on Delivery (COD) across the UAE.</p>
      </div>

      <div style="background: #FFFFFF; padding: 2.25rem; border-radius: 12px; border: 1px solid rgba(233, 223, 213, 0.8);">
        <h3 style="font-size: 1.15rem; font-weight: 700; margin-bottom: 0.75rem;">4. Customer-Focused Support</h3>
        <p style="color: var(--color-text-muted); font-size: 0.875rem;">Dedicated concierge team available 7 days a week via WhatsApp and email to assist your beauty regimen.</p>
      </div>
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Why Choose Us",
  "settings": [
    {
      "type": "text",
      "id": "heading",
      "label": "Heading",
      "default": "Why Choose FABFaddons?"
    }
  ],
  "presets": [
    {
      "name": "Why Choose Us"
    }
  ]
}
{% endschema %}''')

# 18. sections/brand-story.liquid
write('sections/brand-story.liquid', '''<section style="padding: 5rem 0; background: var(--color-bg);">
  <div class="container" style="max-width: 860px; text-align: center;">
    <span style="color: var(--color-accent); font-size: 0.75rem; letter-spacing: 0.15em; text-transform: uppercase; font-weight: 700; display: block; margin-bottom: 1rem;">
      Brand Philosophy
    </span>
    <h2 style="font-size: 2.5rem; font-weight: 700; margin-bottom: 1.5rem;">
      {{ section.settings.heading | default: 'Beauty Is More Than a Routine.' }}
    </h2>
    <div style="font-size: 1.125rem; color: var(--color-text-muted); line-height: 1.8; space-y: 1.5rem;">
      <p style="margin-bottom: 1.25rem;">
        FABFaddons was founded on the belief that everyday self-care should feel like an intentional luxury. Rather than overwhelming your dressing table with endless fleeting trends, we curate only the most effective, exquisitely designed essentials.
      </p>
      <p>
        From medical-grade sonic facial devices to pure crystal contouring stones and peptide-dense elixirs, every piece in our launch collection is chosen to deliver visible radiance while elevating your daily ritual.
      </p>
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Brand Story",
  "settings": [
    {
      "type": "text",
      "id": "heading",
      "label": "Heading",
      "default": "Beauty Is More Than a Routine."
    }
  ],
  "presets": [
    {
      "name": "Brand Story"
    }
  ]
}
{% endschema %}''')

# 19. sections/customer-reviews.liquid
write('sections/customer-reviews.liquid', '''<section style="padding: 5rem 0; background: #FFFFFF; border-top: 1px solid var(--color-secondary-bg);">
  <div class="container">
    <div style="text-align: center; margin-bottom: 3.5rem;">
      <h2 style="font-size: 2.25rem; font-weight: 700; margin-bottom: 0.5rem;">
        {{ section.settings.heading | default: 'Verified Customer Experiences' }}
      </h2>
      <p style="color: var(--color-text-muted); font-size: 1rem;">
        Genuine reviews from beauty enthusiasts in Dubai, Abu Dhabi, and the Emirates.
      </p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
      <div style="background: var(--color-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--color-secondary-bg);">
        <div style="color: var(--color-accent); margin-bottom: 0.5rem;">★★★★★</div>
        <h4 style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.5rem;">Fast delivery & premium feel</h4>
        <p style="font-size: 0.875rem; color: var(--color-text-muted); margin-bottom: 1rem;">"The Aura sonic device arrived within 24 hours to Dubai Marina. After three days my pores feel so much cleaner."</p>
        <span style="font-size: 0.75rem; font-weight: 600; color: var(--color-primary);">Reem A. · Dubai Marina</span>
      </div>

      <div style="background: var(--color-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--color-secondary-bg);">
        <div style="color: var(--color-accent); margin-bottom: 0.5rem;">★★★★★</div>
        <h4 style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.5rem;">Pure liquid glow</h4>
        <p style="font-size: 0.875rem; color: var(--color-text-muted); margin-bottom: 1rem;">"Living with AC all day usually dries my skin. The Aurēlia serum absorbs instantly with zero stickiness."</p>
        <span style="font-size: 0.75rem; font-weight: 600; color: var(--color-primary);">Mariam K. · Abu Dhabi</span>
      </div>

      <div style="background: var(--color-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--color-secondary-bg);">
        <div style="color: var(--color-accent); margin-bottom: 0.5rem;">★★★★★</div>
        <h4 style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.5rem;">Airwrap works in humidity</h4>
        <p style="font-size: 0.875rem; color: var(--color-text-muted); margin-bottom: 1rem;">"The Aurora multi-styler holds curls even in UAE summer weather. The standard UAE 3-pin plug is authentic."</p>
        <span style="font-size: 0.75rem; font-weight: 600; color: var(--color-primary);">Fatima N. · Sharjah</span>
      </div>
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Customer Reviews",
  "settings": [
    {
      "type": "text",
      "id": "heading",
      "label": "Heading",
      "default": "Verified Customer Experiences"
    }
  ],
  "presets": [
    {
      "name": "Customer Reviews"
    }
  ]
}
{% endschema %}''')

# 20. sections/newsletter.liquid
write('sections/newsletter.liquid', '''<section style="padding: 5rem 0; background: var(--color-bg); text-align: center;">
  <div class="container" style="max-width: 600px;">
    <h2 style="font-size: 2.25rem; font-weight: 700; margin-bottom: 0.75rem;">
      {{ section.settings.heading | default: 'A Little More Beauty in Your Inbox.' }}
    </h2>
    <p style="color: var(--color-text-muted); font-size: 1rem; margin-bottom: 2rem;">
      {{ section.settings.text | default: 'Be the first to discover new arrivals, beauty essentials and exclusive offers.' }}
    </p>

    {% form 'customer', class: 'newsletter-form' %}
      <input type="hidden" name="contact[tags]" value="newsletter">
      <div style="display: flex; gap: 0.5rem; max-width: 480px; margin: 0 auto;">
        <input
          type="email"
          name="contact[email]"
          value="{{ form.email }}"
          placeholder="Enter your email address"
          required
          style="flex: 1; padding: 0.875rem 1.25rem; border: 1px solid var(--color-secondary-bg); border-radius: 2px; font-size: 0.875rem;"
        >
        <button type="submit" class="btn-primary" style="padding: 0.875rem 1.75rem;">
          Subscribe
        </button>
      </div>
      {%- if form.posted_successfully? -%}
        <p style="color: #2D6A4F; font-size: 0.875rem; margin-top: 1rem;">Thank you for subscribing to FABFaddons.</p>
      {%- endif -%}
    {% endform %}
  </div>
</section>

{% schema %}
{
  "name": "Newsletter",
  "settings": [
    {
      "type": "text",
      "id": "heading",
      "label": "Heading",
      "default": "A Little More Beauty in Your Inbox."
    },
    {
      "type": "textarea",
      "id": "text",
      "label": "Text",
      "default": "Be the first to discover new arrivals, beauty essentials and exclusive offers."
    }
  ],
  "presets": [
    {
      "name": "Newsletter"
    }
  ]
}
{% endschema %}''')

# 21. sections/footer.liquid
write('sections/footer.liquid', '''<footer style="background: var(--color-primary); color: #F7F3ED; padding: 5rem 0 2rem; border-top: 1px solid rgba(255,255,255,0.05);">
  <div class="container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 3rem; margin-bottom: 4rem;">
    <div>
      <span style="font-family: var(--font-heading); font-size: 1.5rem; font-weight: 700; color: #FFFFFF; display: block; margin-bottom: 0.75rem;">
        FABFaddons
      </span>
      <p style="color: rgba(247, 243, 237, 0.75); font-size: 0.875rem; line-height: 1.6; margin-bottom: 1rem;">
        Modern luxury beauty destination headquartered in Dubai, UAE. Curating premium skincare devices, botanical formulas, and architectural vanity essentials.
      </p>
      <p style="color: var(--color-accent); font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase;">
        Beauty. Confidence. You.
      </p>
    </div>

    <div>
      <h4 style="font-size: 0.875rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--color-accent); margin-bottom: 1.25rem;">
        Quick Links
      </h4>
      <ul style="list-style: none; space-y: 0.6rem; font-size: 0.875rem;">
        <li><a href="{{ routes.root_url }}" style="color: rgba(247, 243, 237, 0.8);">Home</a></li>
        <li><a href="{{ routes.all_products_collection_url }}" style="color: rgba(247, 243, 237, 0.8);">Shop All</a></li>
        <li><a href="/pages/about" style="color: rgba(247, 243, 237, 0.8);">About Us</a></li>
        <li><a href="/pages/contact" style="color: rgba(247, 243, 237, 0.8);">Contact</a></li>
      </ul>
    </div>

    <div>
      <h4 style="font-size: 0.875rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--color-accent); margin-bottom: 1.25rem;">
        Client Concierge
      </h4>
      <ul style="list-style: none; space-y: 0.6rem; font-size: 0.875rem;">
        <li><a href="/pages/faq" style="color: rgba(247, 243, 237, 0.8);">FAQ</a></li>
        <li><a href="/pages/shipping-policy" style="color: rgba(247, 243, 237, 0.8);">Shipping Policy (UAE)</a></li>
        <li><a href="/pages/returns-policy" style="color: rgba(247, 243, 237, 0.8);">Returns & Refunds</a></li>
        <li><a href="/pages/privacy-policy" style="color: rgba(247, 243, 237, 0.8);">Privacy Policy</a></li>
        <li><a href="/pages/terms" style="color: rgba(247, 243, 237, 0.8);">Terms & Conditions</a></li>
      </ul>
    </div>

    <div>
      <h4 style="font-size: 0.875rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--color-accent); margin-bottom: 1.25rem;">
        UAE Payment & Security
      </h4>
      <p style="font-size: 0.8125rem; color: rgba(247, 243, 237, 0.75); margin-bottom: 1rem;">
        Visa, Mastercard, Apple Pay, Cash on Delivery, Tabby & Tamara installments.
      </p>
      <div style="font-size: 0.75rem; color: rgba(247, 243, 237, 0.6);">
        Protected by Shopify 256-Bit SSL Encryption.
      </div>
    </div>
  </div>

  <div class="container" style="padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; font-size: 0.75rem; color: rgba(247, 243, 237, 0.6);">
    <p>&copy; {{ 'now' | date: '%Y' }} FABFaddons. All rights reserved.</p>
    <p>Shopify Online Store 2.0 Native Theme · Designed for UAE Beauty Dropshipping</p>
  </div>
</footer>

{% schema %}
{
  "name": "Footer",
  "settings": []
}
{% endschema %}''')

# 22. sections/main-product.liquid
write('sections/main-product.liquid', '''<section style="padding: 4rem 0; background: var(--color-bg);">
  <div class="container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 4rem;">
    <!-- Gallery -->
    <div>
      {%- if product.featured_media -%}
        {{ product.featured_media | image_url: width: 800 | image_tag: loading: 'eager', style: 'border-radius: 12px; width: 100%; border: 1px solid var(--color-secondary-bg);' }}
      {%- else -%}
        <div style="aspect-ratio: 1; background: var(--color-secondary-bg); border-radius: 12px;"></div>
      {%- endif -%}
    </div>

    <!-- Purchase Module -->
    <div>
      <span style="font-size: 0.75rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--color-accent); font-weight: 700; display: block; margin-bottom: 0.5rem;">
        {{ product.type | default: 'Luxury Beauty' }}
      </span>
      <h1 style="font-size: 2.25rem; font-weight: 700; margin-bottom: 1rem; color: var(--color-primary);">
        {{ product.title }}
      </h1>

      <div style="font-size: 1.5rem; font-weight: 700; color: var(--color-primary); margin-bottom: 1.5rem;">
        {{ product.price | money }}
        {%- if product.compare_at_price > product.price -%}
          <span style="font-size: 1.1rem; color: var(--color-text-muted); text-decoration: line-through; margin-left: 0.5rem;">
            {{ product.compare_at_price | money }}
          </span>
        {%- endif -%}
      </div>

      <div style="background: #FFFFFF; padding: 1rem 1.25rem; border-radius: 8px; border: 1px solid var(--color-secondary-bg); margin-bottom: 2rem; font-size: 0.8125rem; color: var(--color-text);">
        <strong>UAE Delivery:</strong> 1–2 business days across Dubai, Abu Dhabi and the Emirates.<br>
        <strong>Payment:</strong> Cash on Delivery (COD) & Apple Pay supported.
      </div>

      {% form 'product', product %}
        <input type="hidden" name="id" value="{{ product.selected_or_first_available_variant.id }}">
        
        <div style="display: flex; gap: 1rem; margin-bottom: 1.5rem;">
          <input type="number" name="quantity" value="1" min="1" style="width: 80px; padding: 0.875rem; border: 1px solid var(--color-secondary-bg); border-radius: 2px; text-align: center;">
          <button type="submit" class="btn-primary" style="flex: 1;">
            {{ 'products.product.add_to_cart' | t }}
          </button>
        </div>
      {% endform %}

      <div style="margin-top: 2.5rem; border-top: 1px solid var(--color-secondary-bg); padding-top: 1.5rem; line-height: 1.7; font-size: 0.95rem; color: var(--color-text-muted);">
        {{ product.description }}
      </div>
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Product Information",
  "settings": []
}
{% endschema %}''')

# 23. sections/main-collection.liquid
write('sections/main-collection.liquid', '''<section style="padding: 4rem 0; background: var(--color-bg);">
  <div class="container">
    <div style="text-align: center; margin-bottom: 3rem;">
      <h1 style="font-size: 2.5rem; font-weight: 700; margin-bottom: 0.5rem;">
        {{ collection.title | default: 'Shop All Beauty' }}
      </h1>
      <p style="color: var(--color-text-muted); font-size: 1rem;">
        {{ collection.description | default: 'Explore our complete catalog of luxury beauty essentials.' }}
      </p>
    </div>

    <div class="product-grid">
      {%- for product in collection.products -%}
        {% render 'product-card', product: product %}
      {%- else -%}
        <p style="text-align: center; grid-column: 1 / -1; color: var(--color-text-muted);">No products found in this collection.</p>
      {%- endfor -%}
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Collection Grid",
  "settings": []
}
{% endschema %}''')

# 24. sections/main-cart.liquid
write('sections/main-cart.liquid', '''<section style="padding: 4rem 0; background: var(--color-bg);">
  <div class="container" style="max-width: 800px;">
    <h1 style="font-size: 2.5rem; font-weight: 700; margin-bottom: 2rem; text-align: center;">
      {{ 'sections.cart.title' | t }}
    </h1>

    {%- if cart.item_count == 0 -%}
      <div style="text-align: center; padding: 4rem 0;">
        <p style="color: var(--color-text-muted); font-size: 1.1rem; margin-bottom: 1.5rem;">
          {{ 'sections.cart.empty' | t }}
        </p>
        <a href="{{ routes.all_products_collection_url }}" class="btn-primary">
          {{ 'general.continue_shopping' | t }}
        </a>
      </div>
    {%- else -%}
      <form action="{{ routes.cart_url }}" method="post">
        <div style="background: #FFFFFF; border: 1px solid var(--color-secondary-bg); border-radius: 12px; padding: 2rem; margin-bottom: 2rem;">
          {%- for item in cart.items -%}
            <div style="display: flex; gap: 1.5rem; padding-bottom: 1.5rem; margin-bottom: 1.5rem; border-bottom: 1px solid var(--color-secondary-bg); align-items: center;">
              {%- if item.image -%}
                <img src="{{ item.image | image_url: width: 140 }}" alt="{{ item.title }}" style="width: 80px; height: 80px; object-fit: cover; border-radius: 6px;">
              {%- endif -%}
              <div style="flex: 1;">
                <h3 style="font-size: 1.1rem; font-weight: 600;"><a href="{{ item.url }}">{{ item.product.title }}</a></h3>
                <p style="font-size: 0.85rem; color: var(--color-text-muted);">{{ item.variant.title }}</p>
                <div style="margin-top: 0.5rem; display: flex; align-items: center; gap: 1rem;">
                  <span>Qty: {{ item.quantity }}</span>
                  <a href="{{ item.url_to_remove }}" style="font-size: 0.8rem; color: #D90429;">Remove</a>
                </div>
              </div>
              <div style="font-size: 1.1rem; font-weight: 700; color: var(--color-primary);">
                {{ item.final_line_price | money }}
              </div>
            </div>
          {%- endfor -%}

          <div style="display: flex; justify-content: space-between; font-size: 1.25rem; font-weight: 700; padding-top: 1rem;">
            <span>{{ 'sections.cart.subtotal' | t }}</span>
            <span>{{ cart.total_price | money }}</span>
          </div>
        </div>

        <div style="display: flex; justify-content: flex-end; gap: 1rem;">
          <button type="submit" name="checkout" class="btn-primary" style="padding: 1rem 3rem;">
            {{ 'sections.cart.checkout' | t }}
          </button>
        </div>
      </form>
    {%- endif -%}
  </div>
</section>

{% schema %}
{
  "name": "Cart Page",
  "settings": []
}
{% endschema %}''')

# 25. JSON Templates (Online Store 2.0)
write('templates/index.json', '''{
  "sections": {
    "hero": {
      "type": "hero-banner",
      "settings": {
        "subheading": "HAUTE LUXURY BEAUTY · UAE EDITION",
        "heading": "Discover Your Everyday Beauty Ritual.",
        "text": "Explore carefully selected beauty and skincare essentials designed to elevate your everyday routine.",
        "button_label": "SHOP NOW"
      }
    },
    "featured_products": {
      "type": "featured-products",
      "settings": {
        "title": "The Launch Collection",
        "subtitle": "Six meticulously engineered beauty essentials, crafted for modern luxury living.",
        "products_to_show": 6
      }
    },
    "promotional_banner": {
      "type": "promotional-banner",
      "settings": {
        "heading": "Your Beauty. Your Everyday Luxury.",
        "text": "Explore beauty essentials selected to complement your everyday routine."
      }
    },
    "why_choose_us": {
      "type": "why-choose-us",
      "settings": {
        "heading": "Why Choose FABFaddons?"
      }
    },
    "brand_story": {
      "type": "brand-story",
      "settings": {
        "heading": "Beauty Is More Than a Routine."
      }
    },
    "customer_reviews": {
      "type": "customer-reviews",
      "settings": {
        "heading": "Verified Customer Experiences"
      }
    },
    "newsletter": {
      "type": "newsletter",
      "settings": {
        "heading": "A Little More Beauty in Your Inbox."
      }
    }
  },
  "order": [
    "hero",
    "featured_products",
    "promotional_banner",
    "why_choose_us",
    "brand_story",
    "customer_reviews",
    "newsletter"
  ]
}''')

write('templates/product.json', '''{
  "sections": {
    "main": {
      "type": "main-product",
      "settings": {}
    },
    "customer_reviews": {
      "type": "customer-reviews",
      "settings": {}
    }
  },
  "order": [
    "main",
    "customer_reviews"
  ]
}''')

write('templates/collection.json', '''{
  "sections": {
    "main": {
      "type": "main-collection",
      "settings": {}
    }
  },
  "order": [
    "main"
  ]
}''')

write('templates/cart.json', '''{
  "sections": {
    "main": {
      "type": "main-cart",
      "settings": {}
    }
  },
  "order": [
    "main"
  ]
}''')

write('templates/404.json', '''{
  "sections": {
    "main": {
      "type": "main-page",
      "settings": {}
    }
  },
  "order": [
    "main"
  ]
}''')

write('templates/search.json', '''{
  "sections": {
    "main": {
      "type": "main-collection",
      "settings": {}
    }
  },
  "order": [
    "main"
  ]
}''')

# 26. Create ZIP archive
zip_output = '/app/applet/public/fabfaddons-shopify-theme.zip'
os.makedirs(os.path.dirname(zip_output), exist_ok=True)

with zipfile.ZipFile(zip_output, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, BASE_DIR)
            zipf.write(file_path, arcname)

print(f"Successfully generated Shopify Theme ZIP at {zip_output} ({os.path.getsize(zip_output)} bytes)")
