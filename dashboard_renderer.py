def get_dashboard_html():
    css = """
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Inter', sans-serif; background-color: #f4f6f9; color: #333; }
    .app-container { display: flex; height: 100vh; overflow: hidden; }
    .sidebar { width: 250px; background-color: #fff; border-right: 1px solid #eee; display: flex; flex-direction: column; }
    .search-box { padding: 15px; border-bottom: 1px solid #eee; }
    .search-box input { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 6px; outline: none; }
    .nav-menu { flex: 1; overflow-y: auto; padding: 10px 0; }
    .nav-item { padding: 12px 20px; display: flex; align-items: center; justify-content: space-between; cursor: pointer; color: #444; font-size: 14px; text-decoration: none; }
    .nav-item-content { display: flex; align-items: center; gap: 15px; }
    .nav-item:hover { background-color: #f8f9fa; }
    .nav-item.active { background-color: #9c27b0; color: #fff; font-weight: 600; border-radius: 0 25px 25px 0; margin-right: 15px; }
    
    /* Sub Menu */
    .sub-menu { display: none; flex-direction: column; padding-left: 45px; margin-top: 5px; }
    .sub-menu.active { display: flex; }
    .sub-menu-item { padding: 10px 0; font-size: 13px; color: #666; text-decoration: none; display: flex; align-items: center; gap: 10px; cursor: pointer; }
    .sub-menu-item:hover { color: #9c27b0; }
    .sub-menu-item.active { color: #9c27b0; font-weight: 600; }
    .sub-menu-circle { width: 6px; height: 6px; border: 1px solid #ccc; border-radius: 50%; }
    .sub-menu-item.active .sub-menu-circle { border-color: #9c27b0; background-color: #f3e5f5; }
    .main-content { flex: 1; display: flex; flex-direction: column; overflow-y: auto; background-color: #f8f9fa; }
    .top-header { background: #fff; padding: 15px 30px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #eee; }
    .page-title h1 { font-size: 24px; font-weight: 600; margin-bottom: 5px; }
    .breadcrumb { font-size: 13px; color: #777; }
    .breadcrumb span { color: #9c27b0; }
    .content-wrapper { padding: 30px; }
    .theme-preview-card { background: #fff; border-radius: 10px; padding: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.02); margin-bottom: 30px; border: 1px solid #eee; }
    .theme-preview-img { width: 100%; height: 300px; background: #eee; border-radius: 8px; margin-bottom: 15px; background-size: cover; background-position: top; }
    .theme-preview-footer { display: flex; justify-content: space-between; align-items: center; }
    .theme-name { font-size: 18px; font-weight: 600; }
    .btn-primary { background: #9c27b0; color: #fff; padding: 8px 20px; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; }
    .settings-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
    .setting-card { background: #fff; border-radius: 10px; padding: 20px; border: 1px solid #eee; box-shadow: 0 2px 10px rgba(0,0,0,0.02); }
    .setting-header { margin-bottom: 15px; }
    .setting-title { font-size: 15px; font-weight: 600; color: #222; margin-bottom: 5px; }
    .setting-desc { font-size: 12px; color: #777; line-height: 1.4; height: 34px; overflow: hidden; }
    .setting-action { display: flex; justify-content: space-between; align-items: center; border-top: 1px dashed #ddd; padding-top: 15px; }
    .setting-icon { width: 35px; height: 35px; background: #f3e5f5; color: #9c27b0; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 16px; border: 1px dashed #9c27b0; }
    .btn-dark { background: #0f172a; color: #fff; padding: 6px 15px; border: none; border-radius: 4px; cursor: pointer; font-size: 12px; }
    .modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); align-items: center; justify-content: center; z-index: 1000; }
    .modal.active { display: flex; }
    .modal-content { background: #fff; padding: 30px; border-radius: 10px; width: 500px; max-width: 90%; max-height: 90vh; overflow-y: auto; }
    .close-btn { float: right; font-size: 24px; cursor: pointer; }
    .form-group { margin-bottom: 15px; }
    .form-group label { display: block; margin-bottom: 5px; font-size: 13px; font-weight: 600; }
    .form-control { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 6px; }
    .table-container { background: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.02); margin-bottom: 30px; }
    table { width: 100%; border-collapse: collapse; }
    th, td { padding: 12px; text-align: left; border-bottom: 1px solid #eee; font-size: 14px; }
    th { background: #f8f9fa; font-weight: 600; }
    """

    js = """
    document.addEventListener('DOMContentLoaded', () => {
        let allShops = [];
        let currentShop = null;

        // Navigation
        const views = ['dashboard', 'theme', 'brand', 'label', 'category', 'product-list'];
        
        // Handle normal views
        views.forEach(v => {
            const btn = document.getElementById(`nav-${v}`);
            if(btn) {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    
                    // remove active from all sub-menu items and normal nav-items
                    document.querySelectorAll('.nav-item, .sub-menu-item').forEach(i => i.classList.remove('active'));
                    btn.classList.add('active');
                    
                    // highlight parent if it's a sub-menu item
                    if(btn.classList.contains('sub-menu-item')) {
                        document.getElementById('nav-products-toggle').classList.add('active');
                    }

                    views.forEach(view => {
                        const el = document.getElementById(`view-${view}`);
                        if(el) el.style.display = (view === v) ? 'block' : 'none';
                    });
                    
                    if (v === 'theme') {
                        document.getElementById('settings-grid').style.display = 'none'; // hide grid initially
                        if(document.getElementById('start-customize-btn')) {
                            document.getElementById('start-customize-btn').style.display = 'inline-block';
                        }
                        if(currentShop) renderThemeSettingsGrid();
                    }
                    if (v === 'product-list') {
                        if(currentShop) fetchProducts();
                    }
                    if (['brand', 'label', 'category'].includes(v)) {
                        if(currentShop) renderSettingsList(v);
                    }
                });
            }
        });

        // Dropdown toggle
        const prodToggle = document.getElementById('nav-products-toggle');
        const prodSubMenu = document.getElementById('products-sub-menu');
        if(prodToggle && prodSubMenu) {
            prodToggle.addEventListener('click', (e) => {
                e.preventDefault();
                prodSubMenu.classList.toggle('active');
            });
        }

        // Modals
        const shopModal = document.getElementById('shop-modal');
        const settingModal = document.getElementById('edit-setting-modal');
        const productModal = document.getElementById('product-modal');
        
        const brandModal = document.getElementById('brand-modal');
        const labelModal = document.getElementById('label-modal');
        const categoryModal = document.getElementById('category-modal');
        
        document.getElementById('close-create').addEventListener('click', () => shopModal.classList.remove('active'));
        document.getElementById('close-setting').addEventListener('click', () => settingModal.classList.remove('active'));
        document.getElementById('close-product').addEventListener('click', () => productModal.classList.remove('active'));
        
        document.getElementById('close-brand').addEventListener('click', () => brandModal.classList.remove('active'));
        document.getElementById('close-label').addEventListener('click', () => labelModal.classList.remove('active'));
        document.getElementById('close-category').addEventListener('click', () => categoryModal.classList.remove('active'));
        
        document.getElementById('add-shop-btn').addEventListener('click', () => shopModal.classList.add('active'));
        
        function checkShop() {
            if(!currentShop) { alert("Please select or create a shop first."); return false; }
            return true;
        }

        document.getElementById('add-product-btn').addEventListener('click', () => { 
            if(checkShop()) {
                editingProductId = null;
                document.querySelector('#product-modal h2').textContent = 'Add New Product';
                document.querySelector('#add-product-form button[type="submit"]').textContent = 'Add Product';
                document.getElementById('add-product-form').reset();
                
                const brandSel = document.getElementById('prod-brand');
                const catSel = document.getElementById('prod-category');
                brandSel.innerHTML = '<option value="">None</option>';
                catSel.innerHTML = '<option value="">None</option>';
                (currentShop.settings.brands || []).forEach(b => brandSel.innerHTML += `<option value="${b}">${b}</option>`);
                (currentShop.settings.categories || []).forEach(c => catSel.innerHTML += `<option value="${c}">${c}</option>`);
                productModal.classList.add('active'); 
            }
        });
        document.getElementById('add-brand-btn').addEventListener('click', () => { if(checkShop()) brandModal.classList.add('active'); });
        document.getElementById('add-label-btn').addEventListener('click', () => { if(checkShop()) labelModal.classList.add('active'); });
        document.getElementById('add-category-btn').addEventListener('click', () => { if(checkShop()) categoryModal.classList.add('active'); });

        // Start Customize Button
        const startCustomizeBtn = document.getElementById('start-customize-btn');
        if(startCustomizeBtn) {
            startCustomizeBtn.addEventListener('click', () => {
                document.getElementById('settings-grid').style.display = 'grid';
                startCustomizeBtn.style.display = 'none'; // hide the button after clicking
            });
        }

        // Fetch Shops
        async function fetchShops() {
            const res = await fetch('/api/shops');
            const data = await res.json();
            allShops = data.shops || [];
            renderShopsTable();
            populateShopSelector();
            if(allShops.length > 0 && !currentShop) {
                currentShop = allShops[0];
                renderThemeSettingsGrid();
            }
        }

        function renderShopsTable() {
            const tbody = document.querySelector('#shops-table tbody');
            tbody.innerHTML = '';
            allShops.forEach(shop => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td><strong>${shop.name}</strong></td>
                    <td><a href="/s/${shop.subdomain}" target="_blank">/s/${shop.subdomain}</a></td>
                    <td><a href="/s/${shop.subdomain}" target="_blank" class="btn-dark" style="text-decoration:none;">Visit</a></td>
                `;
                tbody.appendChild(tr);
            });
        }

        function populateShopSelector() {
            const sel = document.getElementById('active-shop-selector');
            sel.innerHTML = '';
            allShops.forEach(s => {
                const opt = document.createElement('option');
                opt.value = s.id;
                opt.textContent = s.name;
                sel.appendChild(opt);
            });
            sel.addEventListener('change', (e) => {
                currentShop = allShops.find(s => s.id === e.target.value);
                renderThemeSettingsGrid();
            });
        }

        // Create Shop
        document.getElementById('create-shop-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const payload = {
                name: document.getElementById('shop-name').value,
                subdomain: document.getElementById('shop-subdomain').value,
                email: document.getElementById('shop-email').value,
                theme: 'stolen'
            };
            const res = await fetch('/api/shops', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(payload) });
            if (res.ok) {
                alert('Shop created successfully!');
                shopModal.classList.remove('active');
                fetchShops();
            }
        });

        // Theme Settings Grid
        const settingConfigs = [
            { id: 'header', title: 'Header & Banner', desc: 'Header settings such as, banner image, hero text.', icon: '📰', fields: [
                { key: 'banner_url', label: 'Banner Image URL', type: 'text' },
                { key: 'hero_title', label: 'Hero Title', type: 'text' },
                { key: 'hero_subtitle', label: 'Hero Subtitle', type: 'text' }
            ]},
            { id: 'home', title: 'Home Page', desc: 'Homepage page settings such as colors.', icon: '📰', fields: [
                { key: 'primary_color', label: 'Primary Brand Color', type: 'color' }
            ]},
            { id: 'footer', title: 'Footer', desc: 'Footer settings such as, copyright text.', icon: '📰', fields: [
                { key: 'footer_text', label: 'Footer Text', type: 'text' }
            ]},
            { id: 'category', title: 'Category Collection', desc: 'Category Collection settings.', icon: '📰', fields: [
                { key: 'categories', label: 'Categories', type: 'category_builder' }
            ]},
            { id: 'contact', title: 'Contact Us & Outlets', desc: 'Contact us settings, outlet locations.', icon: '📰', fields: [
                { key: 'outlets', label: 'Outlets', type: 'outlets_builder' }
            ]}
        ];

        let currentEditSetting = null;

        function renderThemeSettingsGrid() {
            if(!currentShop) return;
            document.getElementById('current-theme-name').textContent = `Editing: ${currentShop.name} (${currentShop.theme} theme)`;
            
            const grid = document.getElementById('settings-grid');
            grid.innerHTML = '';

            settingConfigs.forEach(conf => {
                const card = document.createElement('div');
                card.className = 'setting-card';
                card.innerHTML = `
                    <div class="setting-header">
                        <div class="setting-title">${conf.title}</div>
                        <div class="setting-desc">${conf.desc}</div>
                    </div>
                    <div class="setting-action">
                        <div class="setting-icon">${conf.icon}</div>
                        <button class="btn-dark change-setting-btn" data-id="${conf.id}">Change Setting ⌄</button>
                    </div>
                `;
                grid.appendChild(card);
            });

            document.querySelectorAll('.change-setting-btn').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    const conf = settingConfigs.find(c => c.id === e.target.getAttribute('data-id'));
                    openSettingModal(conf);
                });
            });
        }

        function openSettingModal(conf) {
            currentEditSetting = conf;
            document.getElementById('setting-modal-title').textContent = conf.title;
            const container = document.getElementById('setting-dynamic-fields');
            container.innerHTML = '';

            const settings = currentShop.settings || {};

            conf.fields.forEach(f => {
                const div = document.createElement('div');
                div.className = 'form-group';
                div.innerHTML = `<label>${f.label}</label>`;
                
                let val = settings[f.key] || '';
                if(f.type === 'textarea') {
                    if(typeof val === 'object') val = JSON.stringify(val, null, 2);
                    div.innerHTML += `<textarea id="field-${f.key}" class="form-control" rows="5" style="font-family:monospace;font-size:12px;">${val}</textarea>`;
                } else if (f.type === 'category_builder') {
                    let catList = Array.isArray(val) ? val : [];
                    let builderHtml = `<div id="categories-container">`;
                    catList.forEach((c, i) => {
                        builderHtml += `
                            <div class="category-item" style="border:1px solid #eee; padding:10px; margin-bottom:10px; border-radius:5px; background:#f9f9f9; position:relative;">
                                <span class="remove-category" style="position:absolute; top:5px; right:10px; cursor:pointer; color:red; font-weight:bold;">&times;</span>
                                <input type="text" class="form-control cat-name" value="${c.name || ''}" placeholder="Category Name" style="margin-bottom:5px;">
                                <input type="text" class="form-control cat-image" value="${c.image_url || ''}" placeholder="Image URL">
                            </div>
                        `;
                    });
                    builderHtml += `</div><button type="button" class="btn-dark" id="add-category-item-btn" style="width:100%;">+ Add Category</button>`;
                    div.innerHTML += builderHtml;
                } else if (f.type === 'outlets_builder') {
                    let outletsList = Array.isArray(val) ? val : [];
                    let builderHtml = `<div id="outlets-container">`;
                    outletsList.forEach((o, i) => {
                        builderHtml += `
                            <div class="outlet-item" style="border:1px solid #eee; padding:10px; margin-bottom:10px; border-radius:5px; background:#f9f9f9; position:relative;">
                                <span class="remove-outlet" style="position:absolute; top:5px; right:10px; cursor:pointer; color:red; font-weight:bold;">&times;</span>
                                <input type="text" class="form-control out-name" value="${o.name || ''}" placeholder="Outlet Name" style="margin-bottom:5px;">
                                <input type="text" class="form-control out-address" value="${o.address || ''}" placeholder="Address" style="margin-bottom:5px;">
                                <input type="text" class="form-control out-phone" value="${o.phone || ''}" placeholder="Phone">
                            </div>
                        `;
                    });
                    builderHtml += `</div><button type="button" class="btn-dark" id="add-outlet-btn" style="width:100%;">+ Add Outlet</button>`;
                    div.innerHTML += builderHtml;
                } else if (f.type === 'color') {
                    div.innerHTML += `<input type="color" id="field-${f.key}" value="${val}" style="width:100%; height:40px;">`;
                } else {
                    div.innerHTML += `<input type="text" id="field-${f.key}" class="form-control" value="${val}">`;
                }
                container.appendChild(div);
            });
            
            settingModal.classList.add('active');

            // Attach event listener for adding outlet
            const addOutBtn = document.getElementById('add-outlet-btn');
            if (addOutBtn) {
                addOutBtn.addEventListener('click', () => {
                    const outContainer = document.getElementById('outlets-container');
                    const item = document.createElement('div');
                    item.className = 'outlet-item';
                    item.style = 'border:1px solid #eee; padding:10px; margin-bottom:10px; border-radius:5px; background:#f9f9f9; position:relative;';
                    item.innerHTML = `
                        <span class="remove-outlet" style="position:absolute; top:5px; right:10px; cursor:pointer; color:red; font-weight:bold;">&times;</span>
                        <input type="text" class="form-control out-name" placeholder="Outlet Name" style="margin-bottom:5px;">
                        <input type="text" class="form-control out-address" placeholder="Address" style="margin-bottom:5px;">
                        <input type="text" class="form-control out-phone" placeholder="Phone">
                    `;
                    outContainer.appendChild(item);
                    attachRemoveItemEvents('.remove-outlet');
                });
                attachRemoveItemEvents('.remove-outlet');
            }

            // Attach event listener for adding category
            const addCatBtn = document.getElementById('add-category-item-btn');
            if (addCatBtn) {
                addCatBtn.addEventListener('click', () => {
                    const catContainer = document.getElementById('categories-container');
                    const item = document.createElement('div');
                    item.className = 'category-item';
                    item.style = 'border:1px solid #eee; padding:10px; margin-bottom:10px; border-radius:5px; background:#f9f9f9; position:relative;';
                    item.innerHTML = `
                        <span class="remove-category" style="position:absolute; top:5px; right:10px; cursor:pointer; color:red; font-weight:bold;">&times;</span>
                        <input type="text" class="form-control cat-name" placeholder="Category Name" style="margin-bottom:5px;">
                        <input type="text" class="form-control cat-image" placeholder="Image URL">
                    `;
                    catContainer.appendChild(item);
                    attachRemoveItemEvents('.remove-category');
                });
                attachRemoveItemEvents('.remove-category');
            }
        }

        function attachRemoveItemEvents(selector) {
            document.querySelectorAll(selector).forEach(btn => {
                btn.onclick = function() {
                    this.parentElement.remove();
                };
            });
        }

        document.getElementById('edit-setting-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            if(!currentShop || !currentEditSetting) return;
            
            let newSettings = { ...currentShop.settings };
            
            try {
                currentEditSetting.fields.forEach(f => {
                    if(f.type === 'textarea') {
                        let val = document.getElementById(`field-${f.key}`).value;
                        newSettings[f.key] = JSON.parse(val || '[]');
                    } else if(f.type === 'outlets_builder') {
                        let outlets = [];
                        document.querySelectorAll('.outlet-item').forEach(el => {
                            outlets.push({
                                name: el.querySelector('.out-name').value,
                                address: el.querySelector('.out-address').value,
                                phone: el.querySelector('.out-phone').value
                            });
                        });
                        newSettings[f.key] = outlets;
                    } else if(f.type === 'category_builder') {
                        let categories = [];
                        document.querySelectorAll('.category-item').forEach(el => {
                            categories.push({
                                name: el.querySelector('.cat-name').value,
                                image_url: el.querySelector('.cat-image').value
                            });
                        });
                        newSettings[f.key] = categories;
                    } else {
                        newSettings[f.key] = document.getElementById(`field-${f.key}`).value;
                    }
                });
            } catch(err) {
                alert("Invalid format!");
                return;
            }

            const payload = { settings: newSettings };
            
            const res = await fetch(`/api/shops/${currentShop.id}`, {
                method: 'PUT',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(payload)
            });

            if(res.ok) {
                alert('Settings updated!');
                settingModal.classList.remove('active');
                fetchShops(); // Refresh data
            } else {
                alert('Error updating settings');
            }
        });

        // Helper to render simple settings list
        function renderSettingsList(type) {
            if(!currentShop) return;
            const settingsKey = type + 's'; // brands, labels, categories
            const list = currentShop.settings[settingsKey] || [];
            const tbody = document.querySelector(`#${settingsKey}-table tbody`);
            tbody.innerHTML = '';
            if(list.length === 0) {
                tbody.innerHTML = `<tr><td colspan="2">No ${settingsKey} found.</td></tr>`;
            } else {
                list.forEach(item => {
                    tbody.innerHTML += `<tr><td><strong>${item}</strong></td><td><span style="color:green">Active</span></td></tr>`;
                });
            }
        }

        async function saveSettingItem(type, val) {
            if(!currentShop) return;
            const settingsKey = type + 's';
            let newSettings = { ...currentShop.settings };
            let list = newSettings[settingsKey] || [];
            list.push(val);
            newSettings[settingsKey] = list;

            const res = await fetch(`/api/shops/${currentShop.id}`, {
                method: 'PUT',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ settings: newSettings })
            });

            if(res.ok) {
                alert(type + ' added!');
                currentShop.settings = newSettings; // Update local state
                renderSettingsList(type);
                return true;
            } else {
                alert('Error adding ' + type);
                return false;
            }
        }

        document.getElementById('add-brand-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            if(await saveSettingItem('brand', document.getElementById('brand-name').value)) {
                brandModal.classList.remove('active');
                e.target.reset();
            }
        });

        document.getElementById('add-label-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            if(await saveSettingItem('label', document.getElementById('label-name').value)) {
                labelModal.classList.remove('active');
                e.target.reset();
            }
        });

        document.getElementById('add-category-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            if(await saveSettingItem('category', document.getElementById('category-name').value)) {
                categoryModal.classList.remove('active');
                e.target.reset();
            }
        });

        document.getElementById('add-product-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            if(!currentShop) return;

            const submitBtn = e.target.querySelector('button[type="submit"]');
            submitBtn.disabled = true;
            submitBtn.textContent = 'Uploading...';

            let imageUrl = document.getElementById('prod-image-url').value;
            const fileInput = document.getElementById('prod-image-file');

            if (fileInput.files && fileInput.files[0]) {
                const file = fileInput.files[0];
                const reader = new FileReader();
                reader.readAsDataURL(file);
                reader.onload = async () => {
                    imageUrl = reader.result;
                    await submitProduct(imageUrl);
                    submitBtn.disabled = false;
                    submitBtn.textContent = 'Add Product';
                };
                reader.onerror = () => {
                    alert("Error reading file!");
                    submitBtn.disabled = false;
                    submitBtn.textContent = 'Add Product';
                };
            } else if (imageUrl) {
                await submitProduct(imageUrl);
                submitBtn.disabled = false;
                submitBtn.textContent = 'Add Product';
            } else {
                alert("Please provide an image URL or upload a file.");
                submitBtn.disabled = false;
                submitBtn.textContent = 'Add Product';
            }
        });

        async function submitProduct(imageUrl) {
            const regPrice = parseFloat(document.getElementById('prod-reg-price').value);
            const salePriceVal = document.getElementById('prod-sale-price').value;
            const salePrice = salePriceVal ? parseFloat(salePriceVal) : null;
            
            const payload = {
                shop_id: currentShop.id,
                name: document.getElementById('prod-name').value,
                price: salePrice ? salePrice : regPrice,
                old_price: salePrice ? regPrice : null,
                brand: document.getElementById('prod-brand').value,
                category: document.getElementById('prod-category').value,
                image_url: imageUrl,
                description: document.getElementById('prod-desc').value
            };

            const method = editingProductId ? 'PUT' : 'POST';
            const url = editingProductId ? `/api/products/${editingProductId}` : '/api/products';
            const res = await fetch(url, { method: method, headers: {'Content-Type': 'application/json'}, body: JSON.stringify(payload) });
            
            if (res.ok) {
                alert(editingProductId ? 'Product updated successfully!' : 'Product added successfully!');
                productModal.classList.remove('active');
                document.getElementById('add-product-form').reset();
                editingProductId = null;
                fetchProducts();
            } else {
                alert('Error saving product');
            }
        }

        async function fetchProducts() {
            if(!currentShop) return;
            const res = await fetch(`/api/products?shop_id=${currentShop.id}`);
            if(!res.ok) return;
            const data = await res.json();
            const tbody = document.querySelector('#products-table tbody');
            tbody.innerHTML = '';
            (data.products || []).forEach(p => {
                const brandCatStr = [p.brand, p.category].filter(Boolean).join(' | ');
                const brandCatHtml = brandCatStr ? `<br><small style="color:#2196F3">${brandCatStr}</small>` : '';
                
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td><img src="${p.image_url}" style="width:50px; height:50px; object-fit:cover; border-radius:5px;"></td>
                    <td><strong>${p.name}</strong><br><small style="color:#777">${p.description || ''}</small>${brandCatHtml}</td>
                    <td>
                        ${p.old_price ? `<span style="text-decoration:line-through; color:#999; font-size:12px;">$${p.old_price}</span> <span style="color:#9c27b0; font-weight:bold;">$${p.price}</span>` : `<strong>$${p.price}</strong>`}
                    </td>
                    <td>
                        <button class="btn-dark edit-prod-btn" data-id="${p.id}">Edit</button>
                        <button class="btn-dark del-prod-btn" data-id="${p.id}" style="background:#dc3545; margin-left:5px;">Delete</button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
            
            document.querySelectorAll('.del-prod-btn').forEach(btn => {
                btn.addEventListener('click', async (e) => {
                    if(!confirm('Are you sure you want to delete this product?')) return;
                    const pid = e.target.getAttribute('data-id');
                    const res = await fetch(`/api/products/${pid}`, { method: 'DELETE' });
                    if(res.ok) {
                        alert('Product deleted');
                        fetchProducts();
                    } else {
                        alert('Error deleting product');
                    }
                });
            });

            document.querySelectorAll('.edit-prod-btn').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    const pid = e.target.getAttribute('data-id');
                    const product = data.products.find(x => x.id === pid);
                    if(product) openEditProductModal(product);
                });
            });
        }
        
        let editingProductId = null;
        
        function openEditProductModal(product) {
            editingProductId = product.id;
            
            // Populate dropdowns
            const brandSel = document.getElementById('prod-brand');
            const catSel = document.getElementById('prod-category');
            brandSel.innerHTML = '<option value="">None</option>';
            catSel.innerHTML = '<option value="">None</option>';
            (currentShop.settings.brands || []).forEach(b => brandSel.innerHTML += `<option value="${b}">${b}</option>`);
            (currentShop.settings.categories || []).forEach(c => catSel.innerHTML += `<option value="${c}">${c}</option>`);
            
            document.getElementById('prod-name').value = product.name;
            document.getElementById('prod-brand').value = product.brand || '';
            document.getElementById('prod-category').value = product.category || '';
            
            if (product.old_price) {
                document.getElementById('prod-reg-price').value = product.old_price;
                document.getElementById('prod-sale-price').value = product.price;
            } else {
                document.getElementById('prod-reg-price').value = product.price;
                document.getElementById('prod-sale-price').value = '';
            }
            
            document.getElementById('prod-image-url').value = product.image_url.startsWith('data:') ? '' : product.image_url;
            document.getElementById('prod-image-file').value = '';
            document.getElementById('prod-desc').value = product.description || '';
            
            document.querySelector('#product-modal h2').textContent = 'Edit Product';
            document.querySelector('#add-product-form button[type="submit"]').textContent = 'Update Product';
            productModal.classList.add('active');
        }

        fetchShops();
    });
    """

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SaaS Dashboard</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
        <style>
            {css}
        </style>
    </head>
    <body>
        <div class="app-container">
            <!-- Sidebar -->
            <aside class="sidebar">
                <div class="search-box">
                    <input type="text" placeholder="🔍 Search here...">
                </div>
                <nav class="nav-menu">
                    <a href="#" class="nav-item" id="nav-dashboard">
                        <div class="nav-item-content"><span>🏠</span> Dashboard</div>
                    </a>
                    <a href="#" class="nav-item active" id="nav-theme">
                        <div class="nav-item-content"><span>🎨</span> Theme Customize</div>
                    </a>
                    <a href="#" class="nav-item">
                        <div class="nav-item-content"><span>⚙️</span> Store Setting</div>
                    </a>
                    <a href="#" class="nav-item">
                        <div class="nav-item-content"><span>👥</span> Staff</div>
                    </a>
                    <a href="#" class="nav-item">
                        <div class="nav-item-content"><span>🚚</span> Delivery Boy</div>
                    </a>
                    
                    <div class="nav-dropdown">
                        <a href="#" class="nav-item" id="nav-products-toggle">
                            <div class="nav-item-content"><span>🛍️</span> Products</div>
                            <span style="font-size:10px;">▼</span>
                        </a>
                        <div class="sub-menu" id="products-sub-menu">
                            <a href="#" class="sub-menu-item" id="nav-brand">
                                <div class="sub-menu-circle"></div> Brand
                            </a>
                            <a href="#" class="sub-menu-item" id="nav-label">
                                <div class="sub-menu-circle"></div> Label
                            </a>
                            <a href="#" class="sub-menu-item" id="nav-category">
                                <div class="sub-menu-circle"></div> Category
                            </a>
                            <a href="#" class="sub-menu-item" id="nav-product-list">
                                <div class="sub-menu-circle"></div> Product
                            </a>
                        </div>
                    </div>
                </nav>
            </aside>

            <!-- Main Content -->
            <main class="main-content">
                <header class="top-header">
                    <div></div>
                    <div>Admin Profile</div>
                </header>
                
                <div class="content-wrapper" id="view-dashboard" style="display:none;">
                    <div class="page-title">
                        <h1>Dashboard</h1>
                        <div class="breadcrumb"><span>Home</span> > Dashboard</div>
                    </div>
                    <div class="table-container" style="margin-top:20px;">
                        <div style="display:flex; justify-content:space-between; margin-bottom:15px;">
                            <h3>Your Shops</h3>
                            <button class="btn-primary" id="add-shop-btn">+ Create New Shop</button>
                        </div>
                        <table id="shops-table">
                            <thead><tr><th>Shop Name</th><th>Subdomain</th><th>Action</th></tr></thead>
                            <tbody></tbody>
                        </table>
                    </div>
                </div>

                <div class="content-wrapper" id="view-theme">
                    <div class="page-title">
                        <h1>Themes</h1>
                        <div class="breadcrumb"><span>Home</span> > Themes</div>
                    </div>
                    
                    <div style="margin-top:20px;">
                        <select id="active-shop-selector" class="form-control" style="max-width: 300px; margin-bottom: 20px;"></select>
                    </div>

                    <div class="theme-preview-card">
                        <div class="theme-preview-img" style="background-image: url('https://images.unsplash.com/photo-1441986300917-64674bd600d8?q=80&w=1200&auto=format&fit=crop');"></div>
                        <div class="theme-preview-footer">
                            <div class="theme-name" id="current-theme-name">Stolen Theme</div>
                            <button class="btn-primary" id="start-customize-btn">Customize</button>
                        </div>
                    </div>

                    <div class="settings-grid" id="settings-grid" style="display: none; border-top: 1px solid #eee; padding-top: 20px;">
                        <!-- Cards will be generated via JS -->
                    </div>
                </div>

                <div class="content-wrapper" id="view-brand" style="display:none;">
                    <div class="page-title">
                        <h1>Brand</h1>
                        <div class="breadcrumb"><span>Home</span> > Products > Brand</div>
                    </div>
                    <div class="table-container" style="margin-top:20px;">
                        <button class="btn-primary" id="add-brand-btn" style="margin-bottom:15px;">+ Add New Brand</button>
                        <table id="brands-table"><thead><tr><th>Brand Name</th><th>Status</th></tr></thead><tbody><tr><td colspan="2">No brands found.</td></tr></tbody></table>
                    </div>
                </div>

                <div class="content-wrapper" id="view-label" style="display:none;">
                    <div class="page-title">
                        <h1>Label</h1>
                        <div class="breadcrumb"><span>Home</span> > Products > Label</div>
                    </div>
                    <div class="table-container" style="margin-top:20px;">
                        <button class="btn-primary" id="add-label-btn" style="margin-bottom:15px;">+ Add New Label</button>
                        <table id="labels-table"><thead><tr><th>Label Name</th><th>Status</th></tr></thead><tbody><tr><td colspan="2">No labels found.</td></tr></tbody></table>
                    </div>
                </div>

                <div class="content-wrapper" id="view-category" style="display:none;">
                    <div class="page-title">
                        <h1>Category</h1>
                        <div class="breadcrumb"><span>Home</span> > Products > Category</div>
                    </div>
                    <div class="table-container" style="margin-top:20px;">
                        <button class="btn-primary" id="add-category-btn" style="margin-bottom:15px;">+ Add New Category</button>
                        <table id="categories-table"><thead><tr><th>Category Name</th><th>Status</th></tr></thead><tbody><tr><td colspan="2">No categories found.</td></tr></tbody></table>
                    </div>
                </div>

                <div class="content-wrapper" id="view-product-list" style="display:none;">
                    <div class="page-title">
                        <h1>Product</h1>
                        <div class="breadcrumb"><span>Home</span> > Products > Product</div>
                    </div>
                    <div class="table-container" style="margin-top:20px;">
                        <button class="btn-primary" id="add-product-btn" style="margin-bottom:15px;">+ Add New Product</button>
                        <table id="products-table">
                            <thead><tr><th>Image</th><th>Name</th><th>Price</th><th>Action</th></tr></thead>
                            <tbody></tbody>
                        </table>
                    </div>
                </div>
            </main>
        </div>

        <!-- Modals -->
        <div id="shop-modal" class="modal">
            <div class="modal-content">
                <span class="close-btn" id="close-create">&times;</span>
                <h2>Create Shop</h2>
                <form id="create-shop-form" style="margin-top:15px;">
                    <div class="form-group">
                        <label>Shop Name</label>
                        <input type="text" id="shop-name" class="form-control" required>
                    </div>
                    <div class="form-group">
                        <label>Subdomain</label>
                        <input type="text" id="shop-subdomain" class="form-control" required>
                    </div>
                    <div class="form-group">
                        <label>Email</label>
                        <input type="email" id="shop-email" class="form-control" required>
                    </div>
                    <button type="submit" class="btn-primary" style="width:100%;">Create</button>
                </form>
            </div>
        </div>

        <!-- Add Brand Modal -->
        <div id="brand-modal" class="modal">
            <div class="modal-content">
                <span class="close-btn" id="close-brand">&times;</span>
                <h2>Add New Brand</h2>
                <form id="add-brand-form" style="margin-top:15px;">
                    <div class="form-group">
                        <label>Brand Name</label>
                        <input type="text" id="brand-name" class="form-control" required>
                    </div>
                    <button type="submit" class="btn-primary" style="width:100%;">Save</button>
                </form>
            </div>
        </div>

        <!-- Add Label Modal -->
        <div id="label-modal" class="modal">
            <div class="modal-content">
                <span class="close-btn" id="close-label">&times;</span>
                <h2>Add New Label</h2>
                <form id="add-label-form" style="margin-top:15px;">
                    <div class="form-group">
                        <label>Label Name</label>
                        <input type="text" id="label-name" class="form-control" required>
                    </div>
                    <button type="submit" class="btn-primary" style="width:100%;">Save</button>
                </form>
            </div>
        </div>

        <!-- Add Category Modal -->
        <div id="category-modal" class="modal">
            <div class="modal-content">
                <span class="close-btn" id="close-category">&times;</span>
                <h2>Add New Category</h2>
                <form id="add-category-form" style="margin-top:15px;">
                    <div class="form-group">
                        <label>Category Name</label>
                        <input type="text" id="category-name" class="form-control" required>
                    </div>
                    <button type="submit" class="btn-primary" style="width:100%;">Save</button>
                </form>
            </div>
        </div>

        <div id="edit-setting-modal" class="modal">
            <div class="modal-content">
                <span class="close-btn" id="close-setting">&times;</span>
                <h2 id="setting-modal-title">Edit Setting</h2>
                <form id="edit-setting-form" style="margin-top:15px;">
                    <div id="setting-dynamic-fields"></div>
                    <button type="submit" class="btn-primary" style="width:100%; margin-top:15px;">Save Changes</button>
                </form>
            </div>
        </div>

        <!-- Add Product Modal -->
        <div id="product-modal" class="modal">
            <div class="modal-content" style="width: 600px;">
                <span class="close-btn" id="close-product">&times;</span>
                <h2>Add New Product</h2>
                <p style="color:#777; font-size:13px; margin-bottom: 20px;">Fill out the details below to add a new product to your active store.</p>
                <form id="add-product-form">
                    <div class="form-group">
                        <label>Product Name</label>
                        <input type="text" id="prod-name" class="form-control" placeholder="e.g. Premium T-Shirt" required>
                    </div>
                    <div style="display:flex; gap:15px;">
                        <div class="form-group" style="flex:1;">
                            <label>Brand</label>
                            <select id="prod-brand" class="form-control"></select>
                        </div>
                        <div class="form-group" style="flex:1;">
                            <label>Category</label>
                            <select id="prod-category" class="form-control"></select>
                        </div>
                    </div>
                    <div style="display:flex; gap:15px;">
                        <div class="form-group" style="flex:1;">
                            <label>Regular Price ($)</label>
                            <input type="number" id="prod-reg-price" class="form-control" placeholder="0.00" required>
                        </div>
                        <div class="form-group" style="flex:1;">
                            <label>Sale Price ($)</label>
                            <input type="number" id="prod-sale-price" class="form-control" placeholder="0.00">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Product Image</label>
                        <div style="display:flex; gap:10px; flex-direction:column;">
                            <input type="url" id="prod-image-url" class="form-control" placeholder="Or paste image URL (https://...)">
                            <div style="text-align:center; color:#777; font-size:12px;">— OR —</div>
                            <input type="file" id="prod-image-file" class="form-control" accept="image/*">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Description</label>
                        <textarea id="prod-desc" class="form-control" rows="3" placeholder="Short description of the product..."></textarea>
                    </div>
                    <button type="submit" class="btn-primary" style="width:100%; margin-top:10px; padding:12px;">Add Product</button>
                </form>
            </div>
        </div>

        <script>
            {js}
        </script>
    </body>
    </html>
    """
    return html
