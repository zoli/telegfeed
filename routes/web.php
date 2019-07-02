<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    $settings = config('madeline');
    $MadelineProto = new \danog\MadelineProto\API('session.madeline', $settings);
    $MadelineProto->start();

    $var = $MadelineProto->messages->getHistory([
        'peer' => '@mostafamalekian',
        'offset_id' => 0,
        'offset_date' => 0,
        'add_offset' => 0,
        'limit' => 10,
        'max_id' => 0,
        'min_id' => 0
    ]);
    dd($var);
});
