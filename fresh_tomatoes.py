import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Screentime</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-color: black;
            color: white;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .video-tile {
            margin-bottom: 20px;
            padding-top: 20px;
            padding-bottom: 20px;
        }
        .video-tile:hover {
            background-color: #333;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.video-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the videos when the page loads
        $(document).ready(function () {
          $('.video-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Screentime: Movie and TV Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {video_tiles}
    </div>
  </body>
</html>
'''

# A single video entry html template
video_tile_content = '''
<div class="col-xs-12 col-lg-4 video-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
  <div class="col-xs-6"> 
    <img class="img img-responsive" src="{poster_image_url}">
  </div>
  <div class="col-xs-6">
    <h2>{video_title}</h2>
    <h4>{seasons}</h4>
    <h4>{runtime}</h4>
    <p>{plot}</p>
  </div>
</div>
'''


def create_video_tiles_content(videos):
    # The HTML content for this section of the page
    content = ''
    for video in videos:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', video.trailer_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', video.trailer_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the video with its content filled in
        # Format video tile differently for movies and tv shows
        if hasattr(video, "seasons"):
          content += video_tile_content.format(
            video_title=video.title,
            poster_image_url=video.poster_url,
            trailer_youtube_id=trailer_youtube_id,
            plot=video.plot,
            seasons=video.seasons,
            runtime=""
          )
        else:
          content += video_tile_content.format(
            video_title=video.title,
            poster_image_url=video.poster_url,
            trailer_youtube_id=trailer_youtube_id,
            plot=video.plot,
            runtime=video.run_time,
            seasons=""
          )

        if (videos.index(video) + 1) % 3 == 0:
          content += '<div class="clearfix visible-lg-block"></div>'
        

    return content

def open_videos_page(videos):
  # Create or overwrite the output file
  output_file = open('index.html', 'w')

  # Replace the placeholder for the video tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(video_tiles=create_video_tiles_content(videos))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  #url = os.path.abspath(output_file.name)
  #webbrowser.open('file://' + url, new=2) # open in a new tab, if possible