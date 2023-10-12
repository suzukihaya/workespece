require 'google/apis/youtube_v3'
require 'tk'
require "pry"
require 'csv'
youtube = Google::Apis::YoutubeV3::YouTubeService.new
youtube.key = "AIzaSyBAumKLd9grZ04Gb7NekNmDoevFys3vsDU"
$var = TkVariable.new('')
$one='' 

def you() 
  youtube = Google::Apis::YoutubeV3::YouTubeService.new
  youtube.key = "AIzaSyBAumKLd9grZ04Gb7NekNmDoevFys3vsDU"
  youtube_search_list = youtube.list_searches("id,snippet", type: "video", q: $var, max_results: 50)

  $text = ''
  youtube_search_list.items.each do |item|
    title = item.snippet.title
    video_id = item.id.video_id

    $text +=<<~EOS
    #{title}
    https://www.youtube.com/watch?v=#{video_id}
    EOS
  end
  test = File.open('test.csv','a')
  test.puts [$text]
  test.close 
  $var='' 
  
end


TkEntry.new(nil,
   textvariable: $var).pack 

TkButton.new(nil,
    text: '検索&go csv',
    command: proc{you()}).pack


TkButton.new(nil,
    text: 'quit',
    command: proc{exit}).pack



Tk.mainloop
#binding.pry 