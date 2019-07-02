<?php

return [

    'app_info' => [
    	'api_id' => env('TELEGRAM_API_ID'),
    	'api_hash' => env('TELEGRAM_API_HASH'),
    ],

    'logger' => [
    	'param' => storage_path('logs/madeline.log')
    ]

];
