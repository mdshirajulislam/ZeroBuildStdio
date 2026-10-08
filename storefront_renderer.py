def render_storefront(shop, products=[]):
    theme = shop.get("theme", "stolen")
    settings = shop.get("settings", {})
    shop_name = shop.get("name", "stolen.")
    
    primary_color = settings.get("primary_color", "#ffe000")
    hero_title = settings.get("hero_title", f"Welcome to {shop_name}")
    hero_subtitle = settings.get("hero_subtitle", "We have the best products.")
    banner_url = settings.get("banner_url", "https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=1200&auto=format&fit=crop")
    footer_text = settings.get("footer_text", f"© 2026 {shop_name}")
    
    categories = settings.get("categories", [])
    outlets = settings.get("outlets", [])

    products_html = ""
    for p in products:
        badge_html = f'<div class="badge">{p.get("badge")}</div>' if p.get("badge") else ""
        if theme == "stolen":
            old_price_html = f'<span class="old-price">৳{float(p.get("old_price")):.2f}</span>' if p.get("old_price") else ""
            products_html += f"""
            <div class="product-card">
                <div class="card-image-wrap">
                    <div class="heart-icon">&#9825;</div>
                    <img src="{p.get('image_url')}" alt="{p.get('name')}">
                    {badge_html}
                </div>
                <div class="card-details">
                    <h3>{p.get('name')}</h3>
                    <div class="stars">★★★★★</div>
                    <div class="price-wrap">
                        <span class="price">৳{float(p.get('price')):.2f}</span>
                        {old_price_html}
                    </div>
                </div>
            </div>
            """
        else:
            products_html += f"""
            <div class="product-card" style="border: 1px solid #ccc; padding: 1rem; text-align: center;">
                <img src="{p.get('image_url')}" alt="{p.get('name')}" style="width:100%; height:200px; object-fit:cover;">
                <h3>{p.get('name')}</h3>
                <p><strong>৳{p.get('price')}</strong></p>
                <button class="btn" onclick="alert('Added to cart!')">Buy Now</button>
            </div>
            """

    if not products_html:
        products_html = "<p style='text-align:center;width:100%;'>No products available right now.</p>"

    # Generate Categories HTML
    cats_html = ""
    for c in categories:
        cats_html += f"""
        <div class="cat-card">
            <img src="{c.get('image')}" alt="{c.get('name')}">
            <h4>{c.get('name')}</h4>
            <p>{c.get('count')}</p>
        </div>
        """

    # Generate Outlets HTML
    outlets_html = ""
    for i, o in enumerate(outlets):
        outlets_html += f"""
        <div class="outlet-card">
            <h4>{o.get('name')}</h4>
            <p>📍 {o.get('address')}</p>
            <p>📞 {o.get('phone')}</p>
            <button class="btn-directions">Get Directions</button>
        </div>
        """

    if theme == "stolen":
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{shop_name}</title>
            <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
            <style>
                :root {{ --primary: {primary_color}; --text-dark: #111; --text-muted: #666; --bg-gray: #f5f5f5; }}
                * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Poppins', sans-serif; }}
                body {{ background-color: #f9f9f9; color: var(--text-dark); }}
                
                .navbar {{ background-color: var(--primary); padding: 10px 40px; display: flex; align-items: center; justify-content: space-between; position: sticky; top: 0; z-index: 100; }}
                .navbar-left {{ display: flex; align-items: center; gap: 30px; }}
                .logo {{ font-size: 28px; font-weight: 800; letter-spacing: -1px; text-transform: lowercase; }}
                .nav-links {{ display: flex; gap: 20px; font-weight: 600; font-size: 14px; }}
                .nav-links a {{ text-decoration: none; color: #000; }}
                
                .navbar-center {{ flex: 1; display: flex; justify-content: center; padding: 0 40px; }}
                .search-bar {{ width: 100%; max-width: 500px; padding: 10px 20px; border-radius: 50px; border: none; outline: none; font-size: 14px; background: white; }}
                
                .navbar-right {{ display: flex; gap: 20px; align-items: center; font-size: 20px; }}
                .icon {{ cursor: pointer; }}
                
                .banner-container {{ padding: 20px 40px; }}
                .banner {{ width: 100%; max-width: 1200px; margin: 0 auto; display: block; border-radius: 8px; object-fit: cover; height: 300px; }}

                .container {{ max-width: 1200px; margin: 0 auto; padding: 20px 40px; }}
                .section-title {{ font-size: 24px; font-weight: 700; margin-bottom: 20px; }}

                .categories-wrap {{ display: flex; gap: 20px; overflow-x: auto; padding-bottom: 10px; margin-bottom: 40px; }}
                .cat-card {{ background: white; border-radius: 8px; overflow: hidden; min-width: 150px; text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.05); flex-shrink: 0;}}
                .cat-card img {{ width: 100%; height: 150px; object-fit: cover; background: #e0e0e0; }}
                .cat-card h4 {{ font-size: 14px; padding: 10px 5px 5px; }}
                .cat-card p {{ font-size: 12px; color: var(--text-muted); padding-bottom: 10px; }}

                .products-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; margin-bottom: 60px; }}
                .product-card {{ background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.05); position: relative; }}
                .card-image-wrap {{ position: relative; background: #f0f0f0; }}
                .card-image-wrap img {{ width: 100%; height: 250px; object-fit: cover; display: block; }}
                .heart-icon {{ position: absolute; top: 10px; right: 10px; background: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; cursor: pointer; box-shadow: 0 2px 5px rgba(0,0,0,0.1); z-index: 2; }}
                .badge {{ position: absolute; bottom: 10px; right: 10px; background: var(--primary); color: #000; font-size: 10px; font-weight: 700; padding: 2px 6px; border-radius: 4px; text-transform: uppercase; z-index: 2; }}
                .card-details {{ padding: 15px; }}
                .card-details h3 {{ font-size: 13px; font-weight: 600; margin-bottom: 5px; color: #333; }}
                .stars {{ color: #facc15; font-size: 14px; margin-bottom: 10px; letter-spacing: 2px; }}
                .price-wrap {{ display: flex; align-items: center; gap: 10px; }}
                .price {{ font-size: 16px; font-weight: 700; color: #000; }}
                .old-price {{ font-size: 13px; font-weight: 500; color: #ef4444; text-decoration: line-through; }}

                .outlets-section {{ background-color: var(--primary); padding: 50px 40px; text-align: center; }}
                .outlets-section h2 {{ font-size: 28px; font-weight: 700; margin-bottom: 30px; }}
                .outlets-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; max-width: 1200px; margin: 0 auto; }}
                .outlet-card {{ background: white; padding: 25px; border-radius: 12px; text-align: left; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }}
                .outlet-card h4 {{ font-size: 16px; font-weight: 600; margin-bottom: 15px; color: #333; }}
                .outlet-card p {{ font-size: 13px; color: #555; margin-bottom: 10px; display: flex; gap: 10px; align-items: flex-start; }}
                .btn-directions {{ background: #d97706; color: white; border: none; padding: 10px 20px; border-radius: 50px; font-weight: 600; cursor: pointer; margin-top: 10px; font-size: 13px; }}

                footer {{ background-color: #1e1b4b; color: white; padding: 60px 40px 20px; }}
                .footer-grid {{ max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 40px; }}
                .footer-logo {{ font-size: 32px; font-weight: 800; margin-bottom: 20px; }}
                .newsletter input {{ width: 100%; padding: 12px; border-radius: 50px; border: none; outline: none; margin-bottom: 10px; margin-top: 10px; font-size: 13px; }}
                .footer-col h4 {{ font-size: 16px; font-weight: 600; margin-bottom: 20px; }}
                .footer-col ul {{ list-style: none; }}
                .footer-col ul li {{ font-size: 13px; color: #cbd5e1; margin-bottom: 12px; }}
                .footer-bottom {{ text-align: center; border-top: 1px solid rgba(255,255,255,0.1); margin-top: 50px; padding-top: 20px; font-size: 12px; color: #94a3b8; }}
            </style>
        </head>
        <body>
            <div class="navbar">
                <div class="navbar-left">
                    <div class="logo">{shop_name}</div>
                    <div class="nav-links">
                        <a href="#">Shop</a>
                        <a href="#">Categories</a>
                        <a href="#">Track Order</a>
                    </div>
                </div>
                <div class="navbar-center">
                    <input type="text" class="search-bar" placeholder="🔍 Search">
                </div>
                <div class="navbar-right">
                    <span class="icon">♡</span>
                    <span class="icon">👤</span>
                    <span class="icon">🛍️</span>
                </div>
            </div>

            <div class="banner-container">
                <img src="{banner_url}" alt="Banner" class="banner">
            </div>

            <div class="container">
                <h2 class="section-title">Browse by Categories</h2>
                <div class="categories-wrap">
                    {cats_html}
                </div>

                <h2 class="section-title">Most Popular</h2>
                <div class="products-grid">
                    {products_html}
                </div>
            </div>

            <div class="outlets-section">
                <h2 style="font-size:16px; margin-bottom:5px; text-transform:uppercase;">Visit Us</h2>
                <h2>Our Outlets</h2>
                <div class="outlets-grid">
                    {outlets_html}
                </div>
            </div>

            <footer>
                <div class="footer-grid">
                    <div class="footer-col">
                        <div class="footer-logo">{shop_name}</div>
                        <p style="font-size:13px; font-weight:600; margin-bottom:5px;">Subscribe to our newsletter</p>
                        <div class="newsletter" style="position:relative;">
                            <input type="email" placeholder="Your email address">
                            <button style="position:absolute; right:5px; top:15px; background:#d97706; border:none; color:white; padding:5px 15px; border-radius:50px; font-size:12px;">Subscribe</button>
                        </div>
                    </div>
                    <div class="footer-col">
                        <h4>Support</h4>
                        <ul>
                            <li>FAQ</li>
                            <li>Return & Exchange</li>
                            <li>Shipping</li>
                        </ul>
                    </div>
                    <div class="footer-col">
                        <h4>Contact</h4>
                        <ul>
                            <li>✉️ admin@{subdomain if 'subdomain' in locals() else 'shop'}.com</li>
                        </ul>
                    </div>
                </div>
                <div class="footer-bottom">
                    {footer_text}
                </div>
            </footer>
        </body>
        </html>
        """
    else:
        # Generic fallback
        html = f"<html><body><h1>{shop_name}</h1>{products_html}</body></html>"
    return html
