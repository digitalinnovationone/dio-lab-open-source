```php
<?php

namespace Salustiano;

class About extends Me
{
    public function getCurrentWorkplace(): array
    {
        return [
            'workplace' => [
                'company' => null,
                'position' => 'Unemployed'         
            ]
        ];
    }

    public function getDailyKnowledge(): array
    {
        return [
            Php::class,
            Javascript::class,
            Laravel::class,
            Symfony::class,
            CodeIgniter::class,
            Vuejs::class,
            Angular::class,
            ReactNative::class,
            Bootstrap::class,
            TailwindCss::class,
            Aws::class
        ];
    }

    public function getFutureGoal(): string
    {
        return __("Get a Tech Lead position");
    }
}
```