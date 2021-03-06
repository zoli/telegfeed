<?php

namespace Tests\Feature;

use Tests\TestCase;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Foundation\Testing\RefreshDatabase;

class ChannelFeedTest extends TestCase
{
    /**
     * A basic feature test example.
     *
     * @return void
     */
    public function testGetChannelFeed()
    {
        $response = $this->get('/channel/mostafamalekian/feed');

        $response->assertStatus(200);
        $response->assertHeader('content-type', 'text/xml; charset=UTF-8');
    }
}
