// FABFaddons Luxury Cosmetics OS 2.0 Theme JavaScript
document.addEventListener('DOMContentLoaded', () => {
  // Cart Drawer Elements
  const cartTriggers = document.querySelectorAll('[data-cart-drawer-trigger]');
  const cartDrawer = document.querySelector('#cart-drawer');
  const cartOverlay = document.querySelector('#cart-drawer-overlay');
  const cartClose = document.querySelector('[data-cart-drawer-close]');

  function openCart() {
    if (cartDrawer) cartDrawer.classList.add('active');
    if (cartOverlay) cartOverlay.classList.add('active');
    document.body.style.overflow = 'hidden';
    refreshCartDrawer();
  }

  function closeCart() {
    if (cartDrawer) cartDrawer.classList.remove('active');
    if (cartOverlay) cartOverlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  cartTriggers.forEach(t => t.addEventListener('click', openCart));
  if (cartClose) cartClose.addEventListener('click', closeCart);
  if (cartOverlay) cartOverlay.addEventListener('click', closeCart);

  // Mobile Menu Drawer
  const mobileMenuOpen = document.querySelector('#mobile-menu-open');
  const mobileMenuClose = document.querySelector('#mobile-menu-close');
  const mobileMenuDrawer = document.querySelector('#mobile-menu-drawer');

  if (mobileMenuOpen && mobileMenuDrawer) {
    mobileMenuOpen.addEventListener('click', () => {
      mobileMenuDrawer.style.display = 'block';
      document.body.style.overflow = 'hidden';
    });
  }
  if (mobileMenuClose && mobileMenuDrawer) {
    mobileMenuClose.addEventListener('click', () => {
      mobileMenuDrawer.style.display = 'none';
      document.body.style.overflow = '';
    });
  }
  if (mobileMenuDrawer) {
    mobileMenuDrawer.addEventListener('click', (e) => {
      if (e.target === mobileMenuDrawer) {
        mobileMenuDrawer.style.display = 'none';
        document.body.style.overflow = '';
      }
    });
  }

  // Intercept all /cart/add form submissions
  document.addEventListener('submit', async (e) => {
    const form = e.target.closest('form[action*="/cart/add"]');
    if (!form) return;
    e.preventDefault();

    const submitBtn = form.querySelector('[type="submit"]');
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.classList.add('loading');
    }

    try {
      const res = await fetch('/cart/add.js', {
        method: 'POST',
        body: new FormData(form)
      });
      if (res.ok) {
        openCart();
      } else {
        form.submit();
      }
    } catch (err) {
      form.submit();
    } finally {
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.classList.remove('loading');
      }
    }
  });

  // Refresh Cart Drawer Content
  async function refreshCartDrawer() {
    try {
      const res = await fetch('/cart.js');
      const cart = await res.json();
      
      // Update badges
      document.querySelectorAll('[data-cart-count-badge]').forEach(badge => {
        badge.textContent = cart.item_count;
        badge.style.display = cart.item_count > 0 ? 'inline-flex' : 'none';
      });

      // Update drawer subtotal
      const subtotalEl = document.querySelector('[data-cart-drawer-subtotal]');
      if (subtotalEl) {
        subtotalEl.textContent = formatMoney(cart.total_price);
      }

      // Update free shipping bar
      const threshold = (window.themeSettings?.freeShippingThreshold || 250) * 100;
      const progressEl = document.querySelector('[data-shipping-progress]');
      const messageEl = document.querySelector('[data-shipping-message]');
      if (progressEl && messageEl) {
        const percent = Math.min(100, Math.round((cart.total_price / threshold) * 100));
        progressEl.style.width = percent + '%';
        if (cart.total_price >= threshold) {
          messageEl.textContent = window.themeStrings?.freeShippingUnlocked || 'Complimentary UAE Express Delivery Unlocked!';
        } else {
          const away = formatMoney(threshold - cart.total_price);
          messageEl.textContent = (window.themeStrings?.freeShippingAway || 'Add [amount] more for Complimentary Delivery').replace('[amount]', away).replace('{{ amount }}', away);
        }
      }

      // Update line items list in drawer
      const itemsContainer = document.querySelector('#cart-drawer-items-list');
      const emptyContainer = document.querySelector('#cart-drawer-empty-state');
      const footerContainer = document.querySelector('#cart-drawer-footer');

      if (itemsContainer) {
        if (cart.item_count === 0) {
          if (itemsContainer) itemsContainer.style.display = 'none';
          if (emptyContainer) emptyContainer.style.display = 'block';
          if (footerContainer) footerContainer.style.display = 'none';
        } else {
          if (emptyContainer) emptyContainer.style.display = 'none';
          if (footerContainer) footerContainer.style.display = 'block';
          itemsContainer.style.display = 'flex';

          itemsContainer.innerHTML = cart.items.map(item => `
            <li style="display: flex; gap: 1rem; border-bottom: 1px solid var(--color-border); padding-bottom: 1rem; align-items: center;">
              <img src="${item.image || '/assets/hero-luxury-beauty-ritual.jpg'}" alt="${item.title}" style="width: 72px; height: 72px; object-fit: cover; border-radius: 4px; border: 1px solid var(--color-border);">
              <div style="flex: 1;">
                <h4 style="font-size: 0.9rem; font-weight: 700; line-height: 1.3;"><a href="${item.url}" style="color: var(--color-primary);">${item.title}</a></h4>
                <div style="margin-top: 6px; display: flex; justify-content: space-between; align-items: center;">
                  <span style="font-size: 0.825rem; font-weight: 600; color: var(--color-text-muted);">Qty: ${item.quantity}</span>
                  <span style="font-weight: 700; color: var(--color-primary); font-size: 0.95rem;">${formatMoney(item.final_line_price)}</span>
                </div>
              </div>
            </li>
          `).join('');
        }
      }
    } catch (e) {
      console.warn('Could not refresh cart drawer', e);
    }
  }

  function formatMoney(cents) {
    const aed = (cents / 100).toFixed(0);
    return `AED ${aed}`;
  }

  // Variant Pills Handler
  const variantInputs = document.querySelectorAll('input[type="radio"][name="id"]');
  variantInputs.forEach(input => {
    input.addEventListener('change', () => {
      // Update label styling
      input.closest('form').querySelectorAll('.variant-pill-label').forEach(label => {
        label.classList.remove('is-active');
      });
      const currentLabel = input.closest('label');
      if (currentLabel) currentLabel.classList.add('is-active');

      const price = input.dataset.price;
      const comparePrice = input.dataset.comparePrice;
      const available = input.dataset.available === 'true';

      const priceEl = document.querySelector('[data-product-price]');
      if (priceEl && price) priceEl.textContent = price;

      const compareEl = document.querySelector('[data-product-compare-price]');
      if (compareEl) {
        if (comparePrice) {
          compareEl.textContent = comparePrice;
          compareEl.style.display = 'inline';
        } else {
          compareEl.style.display = 'none';
        }
      }

      const addBtn = document.querySelector('[data-add-to-cart-button]');
      if (addBtn) {
        addBtn.disabled = !available;
        addBtn.textContent = available ? (window.themeStrings?.addToBag || 'Add to Bag') : (window.themeStrings?.soldOut || 'Sold Out');
      }
    });
  });

  // Quantity Steppers
  document.querySelectorAll('[data-quantity-btn]').forEach(btn => {
    btn.addEventListener('click', () => {
      const input = btn.parentElement.querySelector('input[name="quantity"]');
      if (!input) return;
      let val = parseInt(input.value) || 1;
      if (btn.dataset.quantityBtn === 'plus') {
        input.value = val + 1;
      } else if (val > 1) {
        input.value = val - 1;
      }
    });
  });

  // Accordion Handler
  document.querySelectorAll('.accordion-header').forEach(header => {
    header.addEventListener('click', () => {
      const content = header.nextElementSibling;
      if (!content) return;
      const isVisible = content.style.display === 'block';
      content.style.display = isVisible ? 'none' : 'block';
      const icon = header.querySelector('.accordion-icon');
      if (icon) {
        icon.textContent = isVisible ? '+' : '−';
      }
    });
  });

  // Wishlist Handling with LocalStorage
  const wishlistKey = 'fabfaddons_wishlist';
  let wishlist = [];
  try {
    wishlist = JSON.parse(localStorage.getItem(wishlistKey) || '[]');
  } catch {
    wishlist = [];
  }

  function updateWishlistUI() {
    document.querySelectorAll('[data-wishlist-id]').forEach(btn => {
      const id = btn.dataset.wishlistId;
      if (wishlist.includes(id)) {
        btn.classList.add('is-active');
      } else {
        btn.classList.remove('is-active');
      }
    });

    // Wishlist count in header
    document.querySelectorAll('[data-wishlist-count]').forEach(el => {
      el.textContent = wishlist.length;
      el.style.display = wishlist.length > 0 ? 'inline-flex' : 'none';
    });
  }
  updateWishlistUI();

  document.addEventListener('click', (e) => {
    const btn = e.target.closest('[data-wishlist-id]');
    if (!btn) return;
    e.preventDefault();
    const id = btn.dataset.wishlistId;
    const index = wishlist.indexOf(id);
    if (index > -1) {
      wishlist.splice(index, 1);
    } else {
      wishlist.push(id);
    }
    localStorage.setItem(wishlistKey, JSON.stringify(wishlist));
    updateWishlistUI();
  });
});
