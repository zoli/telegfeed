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

// Route::get('/', function () {
//     return view('welcome');
// });

Route::get('/telegram/{name}/feed', function ($name) {
    $settings = config('madeline');
    $MadelineProto = new \danog\MadelineProto\API(public_path().'/session.madeline', $settings);
    $MadelineProto->start();

    $id = sprintf('@%s', $name);

    // $channelInfo = $MadelineProto->get_full_info($id);
    $msgBox = $MadelineProto->messages->getHistory([
        'peer' => $id,
        'offset_id' => 0,
        'offset_date' => 0,
        'add_offset' => 0,
        'limit' => 10,
        'max_id' => 0,
        'min_id' => 0
    ]);

    $channel = new class{};
    $channel->title = sprintf('کانال %s', $msgBox['chats'][0]['title']);
    $channel->link = sprintf('https://t.me/%s/', $name);
    $channel->pubDate = date(DATE_RFC2822);
    $channel->lastBuildDate = date(DATE_RFC2822, $msgBox['messages'][0]['date']);
    $channel->posts = [];

    foreach ($msgBox['messages'] as $msg) {
        $post = new class{};
        $post->title = explode("\n", $msg['message'])[0];
        $post->description = $msg['message'];
        $post->link = sprintf('https://t.me/%s/%s', $name, $msg['id']);
        $post->pubDate = date(DATE_RFC2822, $msg['date']);

        array_push($channel->posts, $post);
    }

    return response()
        ->view('channel.feed', compact('channel'))
        ->header('Content-Type', 'text/xml');
});
