---
title: magento 1.4.x cannot login on localhost
author: gjergj.sheldija
layout: post
permalink: /magento-1-4-x-cannot-login-on-localhost/
categories:
  - code
  - magento
  - php
tags:
  - localhost
  - login
  - magento 1.4
comments: true
---
magento 1.4.x stable has a problem on the login procedure on localhost.  
you need to change in app/code/core/Mage/Core/Model/Session/Abstract/Varien.php

```php
// session cookie params
        $cookieParams = array(
            'lifetime' => $cookie->getLifetime(),
            'path'     => $cookie->getPath(),
            'domain'   => $cookie->getConfigDomain(),
            'secure'   => $cookie->isSecure(),
            'httponly' => $cookie->getHttponly()
        );

        if (!$cookieParams['httponly']) {
            unset($cookieParams['httponly']);
            if (!$cookieParams['secure']) {
                unset($cookieParams['secure']);
                if (!$cookieParams['domain']) {
                    unset($cookieParams['domain']);
                }
            }
        }

        if (isset($cookieParams['domain'])) {
            $cookieParams['domain'] = $cookie->getDomain();
        }
```

with

```php
        // session cookie params
        $cookieParams = array(
            'lifetime' => $cookie->getLifetime(),
            'path'     => $cookie->getPath(),
           // 'domain'   => $cookie->getConfigDomain(),
           // 'secure'   => $cookie->isSecure(),
           // 'httponly' => $cookie->getHttponly()
        );
/*
        if (!$cookieParams['httponly']) {
            unset($cookieParams['httponly']);
            if (!$cookieParams['secure']) {
                unset($cookieParams['secure']);
                if (!$cookieParams['domain']) {
                    unset($cookieParams['domain']);
                }
            }
        }

        if (isset($cookieParams['domain'])) {
            $cookieParams['domain'] = $cookie->getDomain();
        }
*/
```