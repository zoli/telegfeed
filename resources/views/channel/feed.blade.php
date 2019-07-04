<?xml version="1.0"?>
<rss version="2.0">
<channel>
    <title>{{ $channel->title }}</title>
    <link>{{ $channel->link }}</link>
    {{-- <description>Liftoff to Space Exploration.</description> --}}
    <language>{{ config('app.locale') }}</language>
    <pubDate>{{ $channel->pubDate }}</pubDate>
    <lastBuildDate>{{ $channel->lastBuildDate }}</lastBuildDate>
    <docs>http://blogs.law.harvard.edu/tech/rss</docs>
    {{-- <generator>Weblog Editor 2.0</generator> --}}
    {{-- <managingEditor>editor@example.com</managingEditor> --}}
    {{-- <webMaster>webmaster@example.com</webMaster> --}}
    @foreach($channel->posts as $post)
    <item>
        <title>{{ $post->title }}</title>
        <link>{{ $post->link }}</link>
        <description>{{ $post->description }}</description>
        <pubDate>{{ $channel->pubDate }}</pubDate>
        <guid>{{ $post->link }}</guid>
    </item>
    @endforeach
</channel>
</rss>
