
    (function() {
      var baseURL = "https://cdn.shopify.com/shopifycloud/checkout-web/assets/";
      var scripts = ["https://cdn.shopify.com/shopifycloud/checkout-web/assets/runtime.baseline.en.e4c3bdaea952b6e55e3a.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/8093.baseline.en.6ba2e21a8f430da0303b.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/6042.baseline.en.e266b34315d5bdd994b0.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/9180.baseline.en.d1203d9b38967896192f.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/app.baseline.en.f51dafe7156539f7b1f1.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/3912.baseline.en.022f5d82209eab358b3e.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/6913.baseline.en.cd70e80d36bc5f065c68.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/4766.baseline.en.0028bb41c208e12ce647.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/6038.baseline.en.e2358c569be512ad8036.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/2354.baseline.en.b863cbb661dbc1937239.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/1847.baseline.en.7ab2be660c39c67760b1.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/3364.baseline.en.d0fb0349886709995da6.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/8783.baseline.en.250a714d58f4496c0cd6.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/5006.baseline.en.83c8646735f5eb63b22a.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/8970.baseline.en.792f086e99b70e21e11f.js","https://cdn.shopify.com/shopifycloud/checkout-web/assets/OnePage.baseline.en.acb35f55c513750490d7.js"];
      var styles = ["https://cdn.shopify.com/shopifycloud/checkout-web/assets/8093.baseline.en.290627c7dcf5603d9c22.css","https://cdn.shopify.com/shopifycloud/checkout-web/assets/app.baseline.en.58e74577ea83789554a9.css","https://cdn.shopify.com/shopifycloud/checkout-web/assets/6268.baseline.en.6a67c0acabb74f73a2d5.css"];
      var fontPreconnectUrls = [];
      var fontPrefetchUrls = [];
      var imgPrefetchUrls = ["https://cdn.shopify.com/s/files/1/0558/1805/files/logo_x320.png?v=1620897080"];

      function preconnect(url, callback) {
        var link = document.createElement('link');
        link.rel = 'dns-prefetch preconnect';
        link.href = url;
        link.crossOrigin = '';
        link.onload = link.onerror = callback;
        document.head.appendChild(link);
      }

      function preconnectAssets() {
        var resources = [baseURL].concat(fontPreconnectUrls);
        var index = 0;
        (function next() {
          var res = resources[index++];
          if (res) preconnect(res[0], next);
        })();
      }

      function prefetch(url, as, callback) {
        var link = document.createElement('link');
        if (link.relList.supports('prefetch')) {
          link.rel = 'prefetch';
          link.fetchPriority = 'low';
          link.as = as;
          if (as === 'font') link.type = 'font/woff2';
          link.href = url;
          link.crossOrigin = '';
          link.onload = link.onerror = callback;
          document.head.appendChild(link);
        } else {
          var xhr = new XMLHttpRequest();
          xhr.open('GET', url, true);
          xhr.onloadend = callback;
          xhr.send();
        }
      }

      function prefetchAssets() {
        var resources = [].concat(
          scripts.map(function(url) { return [url, 'script']; }),
          styles.map(function(url) { return [url, 'style']; }),
          fontPrefetchUrls.map(function(url) { return [url, 'font']; }),
          imgPrefetchUrls.map(function(url) { return [url, 'image']; })
        );
        var index = 0;
        (function next() {
          var res = resources[index++];
          if (res) prefetch(res[0], res[1], next);
        })();
      }

      function onLoaded() {
        preconnectAssets();
        prefetchAssets();
      }

      if (document.readyState === 'complete') {
        onLoaded();
      } else {
        addEventListener('load', onLoaded);
      }
    })();
  