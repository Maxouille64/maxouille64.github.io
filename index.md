Welcome to the Maxouille's official website!
## Projects
<style>
      .dark-mode {
        background: #23272a;
        color: #eee;
      }
      .light-mode {
        background-color: #eee;
        color: #111;
      }
</style>
<div class="project-blurb">
    <div class="project-body">
        <h3><a href="https://github.com/Maxouille64/pokepost" target="_blank"><i aria-hidden="true" class="fab fa-github"></i></a> <a href="http://066644.xyz:5000/" target="_blank">PokePost</a></h3>
        <p style="font-size:12pt;">Backup your builder secretly and share your teams with other people!</p>
    </div>
</div>

<div class="project-blurb">
    <div class="project-body">
        <h3><a href="https://github.com/Maxouille64/RandomTeamBattle" target="_blank"><i aria-hidden="true" class="fab fa-github"></i></a> <a href="https://www.smogon.com/forums/threads/showdown-randomizer-browser-extension.3684255/" target="_blank">PS! Randomizer</a></h3>
        <p style="font-size:12pt;">Play with random team in any format on play.pokemonshowdown.com !</p>
        <a href="https://chromewebstore.google.com/detail/pokemon-showdown-randomiz/dgbjcmccheghgeihjfcmkpfdkdkppolh?hl=en-US" target="_blank"><img src="https://raw.githubusercontent.com/Maxouille64/maxouille64.github.io/refs/heads/main/image/chromestore.png"></a>
<a target="_blank" href="https://addons.mozilla.org/fr/firefox/addon/pokemon-showdown-randomizer/" target="_blank"><img src="https://raw.githubusercontent.com/Maxouille64/maxouille64.github.io/main/EmbeddedImage.png"></a>
    </div>
</div>

<div class="project-blurb">
    <div class="project-body">
        <h3><a href="https://github.com/Maxouille64/InstaCalc" target="_blank"><i aria-hidden="true" class="fab fa-github"></i></a> <a href="https://www.smogon.com/forums/threads/some-client-scripts-3d-models-rtb-instacalc-and-online-builder.3734330/" target="_blank">InstaCalc</a></h3>
        <p style="font-size:12pt;">Automated Calculations for the Official Pokemon showdown damages Calc!</p>
        <a href="https://chromewebstore.google.com/detail/instacalc/jgcdhecmbggngemoioepidjdbaplpeei?hl=en" target="_blank"><img src="https://raw.githubusercontent.com/Maxouille64/maxouille64.github.io/refs/heads/main/image/chromestore.png"></a>
<a target="_blank" href="https://addons.mozilla.org/en-US/firefox/addon/insta-calc/" target="_blank"><img src="https://raw.githubusercontent.com/Maxouille64/maxouille64.github.io/main/EmbeddedImage.png"></a>
    </div>
</div>

<div class="project-blurb">
    <div class="project-body">
        <h3><a href="https://github.com/Maxouille64/PS-3d-Sprites" target="_blank"><i aria-hidden="true" class="fab fa-github"></i></a> <a href="https://www.smogon.com/forums/threads/some-client-scripts-3d-models-rtb-instacalc-and-online-builder.3734330/" target="_blank">PS! 3ds sprites</a></h3>
        <p style="font-size:12pt;"> get Pokemon sprites in 3d !</p>
    </div>
</div>

<div class="project-blurb">
    <div class="project-body">
        <h3><a href="https://github.com/Maxouille64/multibound-py" target="_blank"><i aria-hidden="true" class="fab fa-github"></i></a> <a href="https://github.com/Maxouille64/multibound-py/raw/main/multibound.exe" target="_blank">multibound-py</a></h3>
        <p style="font-size:12pt;">minimal multi-instance Starbound launcher written in python</p>
    </div>
</div>
<button onclick="nuit()" class="button" id="dark">Toggle Dark Mode</button> * Maxouille#3847

<script type="text/javascript">
  function nuit() {
    var body = document.body;
    var currentClass = body.className
    var newClass = body.className == 'dark-mode' ? 'light-mode' : 'dark-mode'
    body.className = newClass

    document.cookie = 'theme=' + (newClass == 'light-mode' ? 'light' : 'dark') + "; expires=Fri, 31 Dec 9999 23:59:59 GMT;"
    console.log('Cookies are now: ' + document.cookie)
  }

  function isDarkThemeSelected() {
    return document.cookie.match(/theme=dark/i) != null
  }

  function setThemeFromCookie() {
    var body = document.body;
    var point = document.getElementById("myMenu");
    body.className = isDarkThemeSelected() ? 'dark-mode' : 'light-mode';
    point.style = isDarkThemeSelected() ? 'list-style-image: url(https://play.pokemonshowdown.com/sprites/itemicons/moon-ball.png)' : 'list-style-image: url(https://play.pokemonshowdown.com/sprites/itemicons/love-ball.png)';
  }

  (function() {
    setThemeFromCookie()
  })();
  function logout() {
    document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    maxFresh();
  }
</script>
