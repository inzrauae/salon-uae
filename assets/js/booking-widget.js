// =============================================
// Fade & Blade â€” Booking Bar Widget
// =============================================
(function () {
    'use strict';

    var BB_SERVICES = [
        // HAIR
        { cat: 'Hair', name: 'Classic Haircut', dur: '30m', price: 100 },
        { cat: 'Hair', name: 'Classic Haircut & Beard', dur: '1h 20m', price: 120 },
        { cat: 'Hair', name: 'Taper Fade', dur: '45m', price: 120 },
        { cat: 'Hair', name: 'Taper Fade & Beard', dur: '1h 35m', price: 140 },
        { cat: 'Hair', name: 'Skin Fade', dur: '1h', price: 140 },
        { cat: 'Hair', name: 'Skin Fade & Beard', dur: '1h 40m', price: 160 },
        { cat: 'Hair', name: 'Kidz Haircut (up to 12 yrs)', dur: '30m', price: 69 },
        { cat: 'Hair', name: 'Hairstyling', dur: '20m', price: 75 },
        { cat: 'Hair', name: 'Shape Up', dur: '30m', price: 85 },
        { cat: 'Hair', name: 'Toppik Hairstyling', dur: '20m', price: 100 },
        { cat: 'Hair', name: 'Head Clean Shave (Razor)', dur: '30m', price: 100 },
        // BEARD
        { cat: 'Beard', name: 'Signature Beard', dur: '45m', price: 110 },
        { cat: 'Beard', name: 'Beard', dur: '30m', price: 70 },
        { cat: 'Beard', name: 'Signature Clean Shave', dur: '45m', price: 100 },
        { cat: 'Beard', name: 'Beard Clean Shave (Razor)', dur: '30m', price: 75 },
        // FACIAL
        { cat: 'Facial', name: 'Express Facial', dur: '30m', price: 200 },
        { cat: 'Facial', name: 'Deep Cleaning', dur: '1h 10m', price: 400 },
        // MASSAGE
        { cat: 'Massage', name: 'Deep Tissue Massage', dur: '1h', price: 360 },
        { cat: 'Massage', name: 'Sports Massage', dur: '1h', price: 360 },
        { cat: 'Massage', name: 'Relaxing Massage', dur: '1h', price: 300 },
        { cat: 'Massage', name: 'Hot Stone', dur: '1h 30m', price: 500 },
        { cat: 'Massage', name: 'Foot Massage', dur: '1h', price: 250 },
        { cat: 'Massage', name: 'Head & Shoulder Massage', dur: '30m', price: 150 },
        { cat: 'Massage', name: 'Hands Massage', dur: '30m', price: 150 },
        { cat: 'Massage', name: 'Hair Wash & Face Massage', dur: '30m', price: 150 },
        // MANICURE & PEDICURE
        { cat: 'Manicure & Pedicure', name: 'Manicure', dur: '30m', price: 90 },
        { cat: 'Manicure & Pedicure', name: 'Pedicure', dur: '30m', price: 110 },
        { cat: 'Manicure & Pedicure', name: 'Manicure & Pedicure', dur: '1h', price: 180 },
        { cat: 'Manicure & Pedicure', name: 'Cut & File Feet', dur: '25m', price: 70 },
        { cat: 'Manicure & Pedicure', name: 'Cut & File Hands', dur: '20m', price: 60 },
        // KERATIN TREATMENT
        { cat: 'Keratin Treatment', name: 'Keratin - Short / Medium Hair', dur: '1h 30m', price: 350 },
        { cat: 'Keratin Treatment', name: 'Keratin - Long Hair', dur: '2h', price: 450 },
        { cat: 'Keratin Treatment', name: 'Keratin - Extra Long Hair', dur: '3h', price: 850 },
        // COLOUR
        { cat: 'Colour', name: 'Hair Dye', dur: '50m', price: 160 },
        { cat: 'Colour', name: 'Beard Dye', dur: '30m', price: 100 },
        // WAXING & TRIMMING
        { cat: 'Waxing & Trimming', name: 'Full Body Waxing', dur: '1h 30m', price: 500 },
        { cat: 'Waxing & Trimming', name: 'Full Leg Waxing', dur: '50m', price: 200 },
        { cat: 'Waxing & Trimming', name: 'Half Leg Waxing', dur: '30m', price: 120 },
        { cat: 'Waxing & Trimming', name: 'Full Arm Waxing', dur: '40m', price: 150 },
        { cat: 'Waxing & Trimming', name: 'Half Arm Waxing', dur: '25m', price: 85 },
        { cat: 'Waxing & Trimming', name: 'Under Arm Waxing', dur: '25m', price: 75 },
        { cat: 'Waxing & Trimming', name: 'Full Back Waxing', dur: '50m', price: 180 },
        { cat: 'Waxing & Trimming', name: 'Chest Waxing', dur: '30m', price: 100 },
        { cat: 'Waxing & Trimming', name: 'Stomach Waxing', dur: '50m', price: 105 },
        { cat: 'Waxing & Trimming', name: 'Half Back Waxing', dur: '40m', price: 110 },
        { cat: 'Waxing & Trimming', name: 'Full Face Waxing', dur: '30m', price: 80 },
        { cat: 'Waxing & Trimming', name: 'Nose Waxing', dur: '10m', price: 35 },
        { cat: 'Waxing & Trimming', name: 'Ear Waxing', dur: '10m', price: 35 },
        { cat: 'Waxing & Trimming', name: 'Ear & Nose Waxing', dur: '25m', price: 60 },
        { cat: 'Waxing & Trimming', name: 'Full Body Hair Trimming', dur: '1h', price: 300 },
        { cat: 'Waxing & Trimming', name: 'Chest Trimming', dur: '30m', price: 100 },
        { cat: 'Waxing & Trimming', name: 'Back Trimming', dur: '30m', price: 100 },
        { cat: 'Waxing & Trimming', name: 'Full Face Threading', dur: '20m', price: 60 },
        { cat: 'Waxing & Trimming', name: 'Eyebrow Shape up', dur: '15m', price: 30 }
    ];

    // Tracks selected services: array of { name, dur, price }
    var selected = [];

    // Expose toggle globally NOW (synchronous â€” no DOMContentLoaded wait needed)
    window.bbTogglePanel = function () {
        var panel = document.getElementById('bb-svc-panel');
        var caret = document.getElementById('bb-svc-caret');
        if (!panel) return;
        if (panel.classList.contains('bb-panel-open')) {
            panel.classList.remove('bb-panel-open');
            if (caret) caret.classList.remove('bb-caret-open');
        } else {
            panel.classList.add('bb-panel-open');
            if (caret) caret.classList.add('bb-caret-open');
        }
    };

    function init() {
        var panelScroll = document.getElementById('bb-panel-scroll');
        if (!panelScroll) return;

        // Build unique category list
        var cats = [];
        BB_SERVICES.forEach(function (s) {
            if (cats.indexOf(s.cat) === -1) cats.push(s.cat);
        });

        // Build panel using divs (no form elements - avoids CSS conflicts)
        var html = '';
        cats.forEach(function (cat) {
            html += '<div class="bb-cat-header">' + cat + '</div>';
            BB_SERVICES.filter(function (s) { return s.cat === cat; }).forEach(function (svc) {
                html +=
                    '<div class="bb-svc-item" data-price="' + svc.price + '" data-name="' + svc.name + '" data-dur="' + svc.dur + '">' +
                    '<span class="bb-svc-check"><i class="fas fa-check"></i></span>' +
                    '<span class="bb-svc-name">' + svc.name + ' <small>' + svc.dur + '</small></span>' +
                    '<span class="bb-svc-price">AED ' + svc.price + '</span>' +
                    '</div>';
            });
        });
        panelScroll.innerHTML = html;

        // Attach click handler to each service item
        var items = panelScroll.querySelectorAll('.bb-svc-item');
        items.forEach(function (item) {
            item.addEventListener('click', function (e) {
                e.stopPropagation();
                toggleItem(item);
            });
        });

        // Close panel on outside click
        document.addEventListener('click', function (e) {
            var seg = document.getElementById('bb-seg-svc');
            if (seg && !seg.contains(e.target)) closePanel();
        });

        // Set minimum date to today
        var dateInp = document.getElementById('bb-date');
        if (dateInp) dateInp.min = new Date().toISOString().split('T')[0];
    }

    function toggleItem(item) {
        var name = item.getAttribute('data-name');
        var price = parseInt(item.getAttribute('data-price'), 10);
        var dur = item.getAttribute('data-dur');
        var idx = -1;
        for (var i = 0; i < selected.length; i++) {
            if (selected[i].name === name) { idx = i; break; }
        }
        if (idx === -1) {
            selected.push({ name: name, price: price, dur: dur });
            item.classList.add('bb-selected');
        } else {
            selected.splice(idx, 1);
            item.classList.remove('bb-selected');
        }
        updateUI();
    }

    function updateUI() {
        var total = 0;
        selected.forEach(function (s) { total += s.price; });

        // Panel footer total
        var panelTotalEl = document.getElementById('bb-panel-total');
        if (panelTotalEl) panelTotalEl.textContent = total;

        // Bar label
        var valEl = document.getElementById('bb-svc-val');
        if (valEl) {
            if (selected.length === 0) valEl.textContent = 'All treatments';
            else if (selected.length === 1) valEl.textContent = selected[0].name;
            else valEl.textContent = selected.length + ' services selected';
        }

        // Summary row below bar
        var summary = document.getElementById('bb-summary');
        var tagsEl = document.getElementById('bb-summary-tags');
        var totalEl = document.getElementById('bb-summary-total');
        if (summary && tagsEl && totalEl) {
            if (selected.length > 0) {
                summary.style.display = 'flex';
                tagsEl.innerHTML = selected.map(function (s) {
                    return '<span class="bb-tag">' + s.name + ' <em>AED ' + s.price + '</em></span>';
                }).join('');
                totalEl.textContent = total;
            } else {
                summary.style.display = 'none';
                tagsEl.innerHTML = '';
            }
        }
    }

    function togglePanel() {
        var panel = document.getElementById('bb-svc-panel');
        var caret = document.getElementById('bb-svc-caret');
        if (!panel) return;
        if (panel.classList.contains('bb-panel-open')) {
            panel.classList.remove('bb-panel-open');
            if (caret) caret.classList.remove('bb-caret-open');
        } else {
            panel.classList.add('bb-panel-open');
            if (caret) caret.classList.add('bb-caret-open');
        }
    }

    function closePanel() {
        var panel = document.getElementById('bb-svc-panel');
        var caret = document.getElementById('bb-svc-caret');
        if (panel) panel.classList.remove('bb-panel-open');
        if (caret) caret.classList.remove('bb-caret-open');
    }

    window.closeBbPanel = function () { closePanel(); };

    window.bbBook = function () {
        if (selected.length === 0) {
            // Open panel to prompt selection
            var panel = document.getElementById('bb-svc-panel');
            var caret = document.getElementById('bb-svc-caret');
            if (panel) panel.classList.add('bb-panel-open');
            if (caret) caret.classList.add('bb-caret-open');
            return;
        }

        var total = 0;
        var lines = [];
        selected.forEach(function (s) {
            total += s.price;
            lines.push('\u2022 ' + s.name + ' (' + s.dur + ') \u2014 AED ' + s.price);
        });

        var locEl = document.getElementById('bb-loc');
        var dateEl = document.getElementById('bb-date');
        var loc = locEl ? locEl.value : 'Dubai';
        var dateStr = '';
        if (dateEl && dateEl.value) {
            var d = new Date(dateEl.value + 'T00:00:00');
            dateStr = '\n\uD83D\uDCC5 Preferred Date: ' + d.toLocaleDateString('en-GB', {
                weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
            });
        }

        var msg =
            '\uD83D\uDC4B Hi Fade & Blade! I\'d like to book the following home service:\n\n' +
            lines.join('\n') +
            '\n\n\uD83D\uDCCD Location: ' + loc +
            dateStr +
            '\n\n\uD83D\uDCB0 Total Estimate: AED ' + total +
            '\n\nPlease confirm availability. Thank you!';

        window.open('https://wa.me/971585887245?text=' + encodeURIComponent(msg), '_blank');
    };

    // Safe init â€” wait for DOM + all scripts ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
