<script setup lang="ts">
  const data = ref([
    {
        "title": "Kendrick Lamar - Mr. Morale & The Big Steppers (2 Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/kendrick-lamar-mr-morale-247x296.jpg",
        "price": "100.00",
        "category": "Hip Hop"
    },
    {
        "title": "Arlo Parks - Collapsed in Sunbeams",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/arlo-parks-collapsed-in-sunbeams-247x296.jpg",
        "price": "400.00",
        "category": "Soul / R & B"
    },
    {
        "title": "Queen - The Game",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/queen-the-game-247x296.jpg",
        "price": "160.00",
        "category": "Hard Rock"
    },
    {
        "title": "The Smile A Light For Attracting Attention (2 Lp amarillo)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/The-Smile-A-Light-for-Attracting-Attention-247x296.jpg",
        "price": "160.00",
        "category": "Indie Rock"
    },
    {
        "title": "Lizzo Special",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/Lizzo-Special-247x296.jpg",
        "price": "180.00",
        "category": "Hip Hop"
    },
    {
        "title": "Luis Alberto Spinetta, Fito Paez la la la (2 Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/spinetta-paez-247x296.jpg",
        "price": "150.00",
        "category": "Rock en Espanol"
    },
    {
        "title": "Michael Jackson History Continues",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/michael-jackson-247x296.jpg",
        "price": "230.00",
        "category": "Pop"
    },
    {
        "title": "King Gizzard And The Lizard Wizard Nonagon Infinity (Vinilo Tricolor)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/king-gizzard-and-the-lizzard-wizard-247x296.jpg",
        "price": "150.00",
        "category": "Rock Alternativo"
    },
    {
        "title": "Justice  - Cross (2 LP)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/justice-cross-247x296.jpg",
        "price": "0.00",
        "category": "Electrónica"
    },
    {
        "title": "The Strokes - The New Abnormal",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/the-stokes-the-new-abnormal-247x296.jpg",
        "price": "135.00",
        "category": "Indie Rock"
    },
    {
        "title": "Cerati / Melero - Colores Santos",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/cerati-melero-colores-santos-247x296.jpg",
        "price": "160.00",
        "category": "Rock en Español"
    },
    {
        "title": "The Beatles - Love (2 Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/beatles1-247x296.jpg",
        "price": "200.00",
        "category": "Clásicos"
    },
    {
        "title": "Rosalía - Motomami (Vinilo Rojo, Poster y Folleto)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/Rosalia-motomami-247x296.jpg",
        "price": "180.00",
        "category": "Pop"
    },
    {
        "title": "John & Yoko* / Plastic Ono Band* With Elephants Memory* And Invisible Strings - Some Time In New York City (2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/john-lennon-some-time-in-new-york-city-247x296.jpg",
        "price": "185.00",
        "category": "Rock" 
    },
    {
        "title": "Kit de Limpieza - Vinyl Styl",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/ultimate-care-kit-247x296.jpg",
        "price": "150.00",
        "category": "Accesorios"
    },
    {
        "title": "Arctic Monkeys - Tranquility Base Hotel + Casino",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/arctic-monkeys-tranquility-base-hotel-casino-247x296.jpg",
        "price": "145.00",
        "category": "Indie Rock"
    },
    {
        "title": "Bowie - Diamond Dogs",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_davidbowie_diamonddogs-247x296.jpg",
        "price": "0.00",
        "category": "Rock"
    },
    {
        "title": "Harry Styles - Harrys House  (Incluye Postal y Folleto de 12 Páginas)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/harrys-house-247x296.jpg",
        "price": "220.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "Red Hot Chili Peppers - Blood Sugar Sex Magik (2 Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/redblood-247x296.jpg",
        "price": "180.00",
        "category": "Rock Alternativo"
    },
    {
        "title": "Ray Charles - The Genius Sings the Blues",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/ray-chares-the-genius-sings-the-blues-247x296.jpg",
        "price": "135.00",
        "category": "Blues"
    },
    {
        "title": "Dire Straits - Brothers In Arms (2 Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/dire-strait-brothers-in-arms-247x296.jpg",
        "price": "150.00",
        "category": "Rock"
    },
    {
        "title": "Jack White - Fear Of The Dawn",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/Jack-White-Fear-Of-The-Dawn-247x296.jpg",
        "price": "125.00",
        "category": "Rock Alternativo"
    },
    {
        "title": "Led Zeppelin - Led Zeppelin III",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_ledzeppelin_III-247x296.jpg",
        "price": "110.00",
        "category": "Hard Rock"
    },
    {
        "title": "Black Sabbath - Heaven And Hell (2 Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/black-sabbath-heaven-and-hell-247x296.jpg",
        "price": "150.00",
        "category": "Metal"
    },
    {
        "title": "Band Of Horses - Things Are Great",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/band-of-horses-things-are-great-247x296.jpg",
        "price": "0.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "Arctic Monkeys - Whatever People Say I Am, Thats What Im Not",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_am_whatever-247x296.jpg",
        "price": "135.00",
        "category": "Indie Rock"
    },
    {
        "title": "Big Brother & The Holding Company - Cheap Thrills",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/CHEAP-THRILLS-A--247x296.jpg",
        "price": "220.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "Khruangbin & Leon Bridges - Texas Moon",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/texxas-moon-247x296.jpg",
        "price": "140.00",
        "category": "Rock Psicodélico"
    },
    {
        "title": "Leon Bridges - Gold-Diggers Sound",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/leon-bridges-Gold-Diggers-Sound-247x296.jpg",
        "price": "200.00",
        "category": "Soul / R & B"
    },
    {
        "title": "Pink Floyd - The Wall (2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/pink-floyd-the-wall-247x296.jpg",
        "price": "160.00",
        "category": "Rock"
    },
    {
        "title": "Prince - Sign \u201cO\u201d The Times (2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/prince-sign-the-times-247x296.jpg",
        "price": "150.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "Talking Heads - Talking Heads: 77",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/talking-heads-77-247x296.jpg",
        "price": "200.00",
        "category": "Clásicos"
    },
    {
        "title": "Lana Del Rey - Chemtrails Over The Country Club",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/Lana-del-Rey-chemtrails-over-country-club-247x296.jpg",
        "price": "0.00",
        "category": "Pop"
    },
    {
        "title": "Queens Of The Stone Age - Songs For The Deaf",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/queenofstoneage1-247x296.jpg",
        "price": "170.00",
        "category": "Hard Rock"
    },
    {
        "title": "Taylor Swift - Folklore",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/taylor-swift-folklore--247x296.jpg",
        "price": "200.00",
        "category": "Indie Rock"
    },
    {
        "title": "Taylor Swift - Lover (Vinilos Rosa + Vinilo Celeste)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/taylor-swift-lover-247x296.jpg",
        "price": "145.00",
        "category": "Pop"
    },
    {
        "title": "King Crimson - Islands",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/king-crimson-islands-247x296.jpg",
        "price": "175.00",
        "category": "Rock Progresivo"
    },
    {
        "title": "Kendrick Lamar - To Pimp A Butterfly (2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/kendrick-lamar-to-pimp-a-butterfly-247x296.jpg",
        "price": "140.00",
        "category": "ESENCIALES"
    },
    {
        "title": "Los Violadores - Y Ahora Qué Pasa, Eh?",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/los-violadores-y-ahora-que-pasa-eh-247x296.jpg",
        "price": "400.00",
        "category": "Rock en Español"
    },
    {
        "title": "Soda Stereo - Sueño Stereo (2 Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/soda-stereo-sueno-stereo-247x296.jpg",
        "price": "220.00",
        "category": "Rock en Español"
    },
    {
        "title": "Bob Marley - Legend",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/Bob-Marley-Legend-247x296.jpg",
        "price": "0.00",
        "category": "Reggae"
    },
    {
        "title": "Twenty One Pilots - Blurryface (2 Lp Vinilo de Color)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/twenty-one-pilots-blurryface.-jpg-247x296.jpg",
        "price": "150.00",
        "category": "Hip Hop"
    },
    {
        "title": "P J Harvey - Rid Of Me",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/pj-harvey-rid-of-me-247x296.jpg",
        "price": "150.00",
        "category": "Indie Rock"
    },
    {
        "title": "Gustavo Cerati - Fuerza Natural (2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/Gustavo-Cerati-Fuerza-Natural-1-247x296.jpg",
        "price": "360.00",
        "category": "Rock en Español"
    },
    {
        "title": "Fito Páez - Circo Beat (2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/fito-paez-circo-beat-247x296.jpg",
        "price": "150.00",
        "category": "Rock en Español"
    },
    {
        "title": "Rata Blanca - Magos Espadas Y Rosas (XX Aniversario En Vivo)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/rata-blanca-magos-espadas-y-rosas-en-vivo-247x296.jpg",
        "price": "150.00",
        "category": "Metal"
    },
    {
        "title": "Childish Gambino - Because The Internet (2 Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/CHILDISH-GAMBINO-because-the-internet-247x296.jpg",
        "price": "250.00",
        "category": "Hip Hop"
    },
    {
        "title": "Angel Olsen - My Woman (Vinyl + Digital)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/angel-olsen-woman-247x296.jpg",
        "price": "200.00",
        "category": "Indie Rock"
    },
    {
        "title": "Pearl Jam - Vs.",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/pearl-jam-vs-247x296.jpg",
        "price": "0.00",
        "category": "Rock Alternativo"
    },
    {
        "title": "Muse - Simulation Theory",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/muse-simulation-theory-247x296.jpg",
        "price": "200.00",
        "category": "Rock Alternativo"
    },
    {
        "title": "J. Cole - 2014 Forest Hills Drive (2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/j-cole-2014-forest-hills-drive-247x296.jpg",
        "price": "120.00",
        "category": "Hip Hop"
    },
    {
        "title": "Sonic Youth - Goo",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_goo_sonicyouth-247x296.jpg",
        "price": "150.00",
        "category": "Indie Rock"
    },
    {
        "title": "Enuff Znuff - Enuff Znuff",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/DiscepSet-172420-247x296.jpg",
        "price": "220.00",
        "category": "Hard Rock"
    },
    {
        "title": "Bob Marley - The Legend",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/bob-marley-the-legend-247x296.jpg",
        "price": "150.00",
        "category": "Reggae"
    },
    {
        "title": "Elvis Presley - The Elvis Presley Collection",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/DiscepSet-201639-247x296.jpg",
        "price": "120.00",
        "category": "Rock & Roll"
    },
    {
        "title": "ElvisPresley  - Back In Memphis",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/DiscepSet-183509-247x296.jpg",
        "price": "150.00",
        "category": "Pop"
    },
    {
        "title": "St. Vincent - Daddys Home",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/st-vincent-daddys-home-247x296.jpg",
        "price": "0.00",
        "category": "Rock Alternativo"
    },
    {
        "title": "George Harrison - All Things Must Pass (50th Anniversary - 3 LP))",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/all-things-must-past-247x296.jpg",
        "price": "150.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "The Beatles - HELP!",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/the-beatles-help-247x296.jpg",
        "price": "200.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "Santana - Santanas Greatest Hits",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/santana-greatest-hits-247x296.jpg",
        "price": "140.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "Various - Rock & Pop Nacional",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/MayVinylAR-28-247x296.jpg",
        "price": "200.00",
        "category": "Rock en Español"
    },
    {
        "title": "Bob Dylan - Bob Dylans Greatest Hits",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/bob-dylan-greatest-hits-247x296.jpg",
        "price": "165.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "Bruce Springsteen - In Concert / MTV Unplugged (2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/bruce-springsteen-in-concert-247x296.jpg",
        "price": "140.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "New Kids On The Block - Hangin Tough",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/new-kids-on-the-block-hangin-tough--247x296.jpg",
        "price": "160.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "Deep Purple - The Battle Rages On!",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/deep-purpple-the-battle-rages-on-247x296.jpg",
        "price": "0.00",
        "category": "Hard Rock"
    },
    {
        "title": "AC/DC - Powerage",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/ac-dc-powerage-247x296.jpg",
        "price": "135.00",
        "category": "Hard Rock"
    },
    {
        "title": "Bruce Springsteen - The Rising (2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/bruce-springsteen-the-rising-247x296.jpg",
        "price": "130.00",
        "category": "Rock"
    },
    {
        "title": "J Dilla - Donuts (2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/j-dilla-donuts-1-247x296.jpg",
        "price": "160.00",
        "category": "Hip Hop"
    },
    {
        "title": "Almendra - Almendra En Obras/2",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/discoAR-41-247x296.jpg",
        "price": "140.00",
        "category": "Rock en Español"
    },
    {
        "title": "Los Fabulosos Cadillacs - Yo Te Avise!!",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/discoAR-25-247x296.jpg",
        "price": "98.00",
        "category": "Rock en Español"
    },
    {
        "title": "Almendra - Almendra",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/1rock-argentino-34-247x296.jpg",
        "price": "180.00",
        "category": "Vinilos de \u00c9poca"
    },
    {
        "title": "Belle & Sebastian - Storytelling",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/belle-and-sebastian-storytelling-247x296.jpg",
        "price": "130.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "Gorillaz - Song Machine Season One",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/gorillaz-song-machine-247x296.jpg",
        "price": "0.00",
        "category": "Pop"
    },
    {
        "title": "Traffic Sound - Traffic Sound",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/traffic-sound-traffic-sound-247x296.jpg",
        "price": "180.00",
        "category": "Nacional"
    },
    {
        "title": "Miles Davis - Bitches Brew (2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/miles-davis-bitches-of-brew-247x296.jpg",
        "price": "120.00",
        "category": "Jazz"
    },
    {
        "title": "Greta Van Fleet - Anthem Of The Peaceful Army",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/gretta-van-fleet-247x296.jpg",
        "price": "190.00",
        "category": "Hard Rock"
    },
    {
        "title": "Guns N Roses - Greatest Hits (2 Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/guns-and-roses-greatest-hits-247x296.jpg",
        "price": "170.00",
        "category": "Hard Rock"
    },
    {
        "title": "Fiona Apple - Fetch The Bolt Cutters (2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/fiona-apple-1-247x296.jpg",
        "price": "165.00",
        "category": "Pop"
    },
    {
        "title": "Blur - Live At The BBC",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/blur-bbc-247x296.jpg",
        "price": "125.00",
        "category": "Brit Pop"
    },
    {
        "title": "Travis Scott - Astroworld (2 Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/travis-scott-247x296.jpg",
        "price": "200.00",
        "category": "Hip Hop"
    },
    {
        "title": "The Beach Boys - Concert",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/beach-boys-concert-a-247x296.jpg",
        "price": "0.00",
        "category": "Pop"
    },
    {
        "title": "Magma - Kohntarkosz",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/MAGMA-1A-247x296.jpg",
        "price": "130.00",
        "category": "Rock Progresivo"
    },
    {
        "title": "Interpol - Marauder",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/Interpol-marauder-247x296.jpg",
        "price": "70.00",
        "category": "Indie Rock"
    },
    {
        "title": "Willie Rosario - La Leyenda De La Salsa",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/WILLIE-ROSARIO-1-A-247x296.jpg",
        "price": "150.00",
        "category": "Salsa"
    },
    {
        "title": "Richie Ray Y Bobby Cruz - Viven",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/RICHIE-RAY-BOBBY-2-A-247x296.jpg",
        "price": "120.00",
        "category": "Salsa"
    },
    {
        "title": "Orquesta Mulenze - Creciendo",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/ORQUESTA-MULENZE-1-A-247x296.jpg",
        "price": "100.00",
        "category": "Salsa"
    },
    {
        "title": "Paquito DRivera - Live At Keystone Korner",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/PAQUITO-3-A-247x296.jpg",
        "price": "100.00",
        "category": "Salsa"
    },
    {
        "title": "Paquito DRivera - Mariel",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/PAQUITO-2-A-247x296.jpg",
        "price": "100.00",
        "category": "Salsa"
    },
    {
        "title": "Tabaco Y Su Orquesta - Cosa Linda",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/TABACO-1-A-247x296.jpg",
        "price": "0.00",
        "category": "Salsa"
    },
    {
        "title": "Fania All Stars - Delicate & Jumpy",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/fania-1-a-247x296.jpg",
        "price": "100.00",
        "category": "Salsa"
    },
    {
        "title": "Led Zeppelin - Something Else**",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/LED-ZEPPELIN-1-A-1-247x296.jpg",
        "price": "65.00",
        "category": "Rock"
    },
    {
        "title": "The Kinks - Golden Hour Of The Kinks Vol. 2",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/the-kinks-1-a-247x296.jpg",
        "price": "130.00",
        "category": "Rock"
    },
    {
        "title": "Wham! - Fantastic",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/wham-1-a-247x296.jpg",
        "price": "100.00",
        "category": "New Wave / Post Punk"
    },
    {
        "title": "John Coltrane - Live At The Village Vanguard Again!",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/john-coltrane-3-a-247x296.jpg",
        "price": "130.00",
        "category": "Jazz"
    },
    {
        "title": "Uriah Heep - Abominog",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/uriah-heep-3-a-247x296.jpg",
        "price": "120.00",
        "category": "Hard Rock"
    },
    {
        "title": "Uriah Heep - Return To Fantasy",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/uriah-heep-1-a-247x296.jpg",
        "price": "70.00",
        "category": "Hard Rock"
    },
    {
        "title": "Miles Davis - Isle Of Wight Concert",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/miles-davis-3-a-247x296.jpg",
        "price": "0.00",
        "category": "Jazz"
    },
    {
        "title": "Jethro Tull - A Passion Play",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/Jethro-Tull-a-passion-play-247x296.jpg",
        "price": "120.00",
        "category": "Rock Progresivo"
    },
    {
        "title": "Roxy Music - The Atlantic Years 1973 - 1980",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/ROXY-MUSIC-1-A-1-247x296.jpg",
        "price": "150.00",
        "category": "Rock"
    },
    {
        "title": "Wishbone Ash - Front Page News",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/wishbone-ash-1-a-247x296.jpg",
        "price": "130.00",
        "category": "Rock"
    },
    {
        "title": "Max Middleton - Fantastic Synthesizer Of Superman",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/SUPERMAN-1-A-247x296.jpg",
        "price": "90.00",
        "category": "Electrónica"
    },
    {
        "title": "Vanilla Fudge - Star-Collection",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/vanilla-fudge-3a-247x296.jpg",
        "price": "140.00",
        "category": "Rock Progresivo"
    },
    {
        "title": "Earthshaker - Shakers Shakies",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/earthshakers-1a-247x296.jpg",
        "price": "130.00",
        "category": "Hard Rock"
    },
    {
        "title": "Wings - London Town *",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/wings-london-town-247x296.jpg",
        "price": "120.00",
        "category": "Rock"
    },
    {
        "title": "Styx - Pieces Of Eight",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/styx-1a-247x296.jpg",
        "price": "0.00",
        "category": "Rock Progresivo"
    },
    {
        "title": "Little Feat - Time Loves A Hero",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/little-feat-1a-247x296.jpg",
        "price": "120.00",
        "category": "Rock"
    },
    {
        "title": "Sui Generis - Lo Mejor De Sui Generis",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/1rock-argentino-6-247x296.jpg",
        "price": "220.00",
        "category": "Rock en Español"
    },
    {
        "title": "Almendra - Almendra",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/1rock-argentino-34-247x296.jpg",
        "price": "200.00",
        "category": "Rock en Español"
    },
    {
        "title": "Charly Garcia - Piano Bar",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/charly-piano-247x296.jpg",
        "price": "135.00",
        "category": "Clásicos"
    },
    {
        "title": "Charles Mingus - Mingus Mingus Mingus Mingus Mingus",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/charles_mingus_-_mingus_mingus_mingus_mingus_-_blue_vinyl_-_dol954hb_-_0889397006136-e1590157616119-247x296.jpg",
        "price": "125.00",
        "category": "Jazz"
    },
    {
        "title": "Lauryn Hill - The Miseducation Of Lauryn Hill",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/lauryn-hill-247x296.jpg",
        "price": "120.00",
        "category": "Hip Hop"
    },
    {
        "title": "Luis Alberto Spinetta - A 18\u2032 Del Sol",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/spinneta-18-247x296.jpg",
        "price": "150.00",
        "category": "Rock en Español"
    },
    {
        "title": "Virus - Wadu-Wadu",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/virus-wadu-wadu-247x296.jpg",
        "price": "0.00",
        "category": "Rock en Español"
    },
    {
        "title": "Los Auténticos Decadentes - \u00a1 Supersonico !",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/los-autenticos-decadentes-247x296.jpg",
        "price": "150.00",
        "category": "Pop"
    },
    {
        "title": "Enanitos Verdes - Carrousel",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/Plantilla-web-1-247x296.jpg",
        "price": "130.00",
        "category": "Rock en Español"
    },
    {
        "title": "Luis Alberto Spinetta - Don Lucero",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/spinetta-247x296.jpg",
        "price": "150.00",
        "category": "Rock en Español"
    },
    {
        "title": "Neil Young - Roxy (Tonights The Night Live)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/neil-young-roxy-247x296.jpg",
        "price": "100.00",
        "category": "Clásicos"
    },
    {
        "title": "The Strokes - Room On Fire",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_thestrokes_roomonfire-247x296.jpg",
        "price": "135.00",
        "category": "Indie Rock"
    },
    {
        "title": "The Doors - The Soft Parade",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/doors2-247x296.jpg",
        "price": "140.00",
        "category": "Rock"
    },
    {
        "title": "The Black Keys - Rubber Factory",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/blackkeys1-247x296.jpg",
        "price": "185.00",
        "category": "Indie Rock"
    },
    {
        "title": "Phoenix - Bankrupt!",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/phoenix-247x296.jpg",
        "price": "0.00",
        "category": "Indie Rock"
    },
    {
        "title": "Lou Reed - Animal Serenade",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/loureed1-247x296.jpg",
        "price": "125.00",
        "category": "Rock"
    },
    {
        "title": "LCD Soundsystem - American Dream",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/lcdsystem-247x296.jpg",
        "price": "120.00",
        "category": "Electrónica"
    },
    {
        "title": "Arcade Fire - Neon Bible (2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/arcade-247x296.jpg",
        "price": "140.00",
        "category": "Indie Rock"
    },
    {
        "title": "Interpol - Antics",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_interpol_antics2-247x296.jpg",
        "price": "160.00",
        "category": "Indie Rock"
    },
    {
        "title": "Eagles - Hotel California",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/hotel-california-247x296.jpg",
        "price": "140.00",
        "category": "Clásicos"
    },
    {
        "title": "Bob Dylan - The Essential (2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/bob-dylan-2-247x296.jpg",
        "price": "130.00",
        "category": "Clásicos"
    },
    {
        "title": "Ahí Vamos - Gustavo Cerati",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/ahí-vamos-247x296.jpg",
        "price": "200.00",
        "category": "Rock en Español"
    },
    {
        "title": "The Beatles - Revolver",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/the-beatles-revolver-vinyl-lp_574x-247x296.png",
        "price": "0.00",
        "category": "Clásicos"
    },
    {
        "title": "The Killers - Hot Fuss",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_thekillers_hotfuss-247x296.jpg",
        "price": "145.00",
        "category": "Indie Rock"
    },
    {
        "title": "Lana Del Rey - Paradise",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/lana-del-rey-paradise-247x296.jpg",
        "price": "200.00",
        "category": "Pop"
    },
    {
        "title": "Arcade Fire - We",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/arcadefire-we-whitevinyl-247x296.jpg",
        "price": "170.00",
        "category": "Indie Rock"
    },
    {
        "title": "Babasonicos - Infame",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/babasonicos-infame-247x296.jpg",
        "price": "150.00",
        "category": "Rock Alternativo"
    },
    {
        "title": "Beach House - 7",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/beach-house-7-247x296.jpg",
        "price": "200.00",
        "category": "Indie Rock"
    },
    {
        "title": "David Bowie - \u2605 (Blackstar) (2 Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/David-Bowie-Blackstar-247x296.jpg",
        "price": "220.00",
        "category": "Electrónica"
    },
    {
        "title": "Almendra - Almendra",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/almendra-almendra-247x296.jpg",
        "price": "240.00",
        "category": "Rock en Español"
    },
    {
        "title": "Liam Gallagher - Cmon You Know (Transparente)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/liam-gallagher-cmon-you-know-247x296.jpg",
        "price": "185.00",
        "category": "Indie Rock"
    },
    {
        "title": "Tool - Lateralus (2 LP)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_tool_lateratus-247x296.jpg",
        "price": "150.00",
        "category": "Metal"
    },
    {
        "title": "Daft Punk - TRON: Legacy  (2 Lp Banda Sonora De La Película)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/6b80f1a63d6514c2647f6ca0726f5be6-247x296.jpg",
        "price": "220.00",
        "category": "Electrónica"
    },
    {
        "title": "Neil Young - Harvest",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/harvest-neil-young-247x296.jpg",
        "price": "170.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "Wet Leg - Wet Leg (Lp Amarillo Con Código De Descarga)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/wet-leg-wet-leg-247x296.jpg",
        "price": "145.00",
        "category": "Indie Rock"
    },
    {
        "title": "King Crimson - In The Court Of The Crimson King",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/kingcrimson-247x296.jpg",
        "price": "135.00",
        "category": "Clásicos"
    },
    {
        "title": "Daft Punk - Random Access Memories (2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/daft-Punk-Random-memory-acces-247x296.jpg",
        "price": "145.00",
        "category": "Electrónica"
    },
    {
        "title": "Lady Gaga - Dawn Of Chromatica",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/Lady-Gaga-Down-of-Chromatica-247x296.jpg",
        "price": "115.00",
        "category": "Electrónica"
    },
    {
        "title": "Nas - Illmatic",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/nas-illnatic-247x296.jpg",
        "price": "220.00",
        "category": "Hip Hop"
    },
    {
        "title": "Pink Floyd - Animals",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_pinkfloyd_animals-247x296.jpg",
        "price": "150.00",
        "category": "Rock Progresivo"
    },
    {
        "title": "Megadeth - A Night In Buenos Aires (3Lp Color Azul)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/CLO2536LP-BLUE-2-247x296.png",
        "price": "150.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "Tame Impala - Currents (2 Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/currents-247x296.jpg",
        "price": "180.00",
        "category": "Indie Rock"
    },
    {
        "title": "Nirvana - MTV Unplugged In New York Lp + Digital",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/Nirvana-247x296.jpg",
        "price": "200.00",
        "category": "Clásicos"
    },
    {
        "title": "Soda Stereo - MTV Unplugged - Comfort y Música Para Volar (Edicion Limitada, transparente)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/Soda-Stereo-Mtv-Unplugged-247x296.jpg",
        "price": "240.00",
        "category": "Rock en Español"
    },
    {
        "title": "Bjork - Post",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_bjork_post-247x296.jpg",
        "price": "140.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "Serú Girán - Serú Girán (Vinilo + Cd)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/seru-giran-seru-giran-247x296.jpg",
        "price": "220.00",
        "category": "Rock en Español"
    },
    {
        "title": "Little Simz - Grey Area",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/LITTLE-SIMZ-GREY-AREA-247x296.jpg",
        "price": "280.00",
        "category": "Hip Hop"
    },
    {
        "title": "Adele - 30 (Dos Discos)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/adele-30-247x296.jpg",
        "price": "220.00",
        "category": "Pop"
    },
    {
        "title": "Rolling Stones - Let It Bleed (50 Th Anniversary Edition)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/DiscepSet-172002-247x296.jpg",
        "price": "280.00",
        "category": "Blues Rock"
    },
    {
        "title": "Ocean - \u201cA\u201d Live + B",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/DiscepSet-171847-247x296.jpg",
        "price": "100.00",
        "category": "Hard Rock"
    },
    {
        "title": "Dio - Holy Diver Live (No sellado)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/DiscepSet-173336-247x296.jpg",
        "price": "150.00",
        "category": "Metal"
    },
    {
        "title": "The Rolling Stones - Gimme Shelter",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/DiscepSet-182718-247x296.jpg",
        "price": "170.00",
        "category": "Rock"
    },
    {
        "title": "Animal Collective - Strawberry Jam (2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/animal-collective-strawberry-jam-247x296.jpg",
        "price": "140.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "The Weeknd - After Hours (2 Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/THE-WEEKND-AFTER-HOURS-247x296.jpg",
        "price": "200.00",
        "category": "Hip Hop"
    },
    {
        "title": "Robert Johnson - King Of The Delta Blues Singers",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/robert-johnson-king-of-the-delta-blues-singers-247x296.jpg",
        "price": "180.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "Pax - Pax (May God And Your Will Land You And Your Soul Miles Away From Evil)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/pax-pax-247x296.jpg",
        "price": "140.00",
        "category": "Rock Progresivo"
    },
    {
        "title": "Alfredo Linares - Lo Que Tengo",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/alfredo-linares-lo-que-tengo-247x296.jpg",
        "price": "180.00",
        "category": "Salsa"
    },
    {
        "title": "Metallica - Ride The Lightning",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_metallica_ridethelightning-247x296.jpg",
        "price": "140.00",
        "category": "Metal"
    },
    {
        "title": "Scorpions - World Wide Live",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/discoep2-29-247x296.jpg",
        "price": "140.00",
        "category": "Hard Rock"
    },
    {
        "title": "Perú Negro - Perú Negro",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/peru-negro-247x296.jpg",
        "price": "125.00",
        "category": "Nacional"
    },
    {
        "title": "Ariana Grande - Dangerous Woman",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/ariana-grande-dangerous-woman-247x296.jpg",
        "price": "135.00",
        "category": "Pop"
    },
    {
        "title": "Pearl Jam - Gigaton",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/pearl-jam-giga-247x296.jpg",
        "price": "200.00",
        "category": "Grunge"
    },
    {
        "title": "Spoon - All The Weird Kids Up Front (Más Rolas Chidas)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/spoon-RSD-a-247x296.jpg",
        "price": "130.00",
        "category": "Indie Rock"
    },
    {
        "title": "The Beatles - Magical Mystery Tour (Incluye libro de 24 páginas)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/the-beatles-magical-mistery-tour-247x296.jpg",
        "price": "140.00",
        "category": "Clásicos"
    },
    {
        "title": "Blue \u00d6yster Cult - On Your Feet Or On Your Knees",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/blue-oyster-1-a-1-247x296.jpg",
        "price": "170.00",
        "category": "Hard Rock"
    },
    {
        "title": "Richie Ray & Bobby Cruz - Back To Back",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/RICHIE-RAY-BOBBY-1-A-247x296.jpg",
        "price": "120.00",
        "category": "Salsa"
    },
    {
        "title": "Mon Rivera Y Su Orquesta - Karakatis-Ki",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/MON-RIVERA-1-A-247x296.jpg",
        "price": "180.00",
        "category": "Salsa"
    },
    {
        "title": "Paquito DRivera - Paquito Blowin",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/PAQUITO-1-A-247x296.jpg",
        "price": "150.00",
        "category": "Salsa"
    },
    {
        "title": "Grand Funk - All The Girls In The World Beware !!!",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/Grandfunk-1-a-247x296.jpg",
        "price": "100.00",
        "category": "Hard Rock"
    },
    {
        "title": "Julio Iglesias - Por Una Mujer",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/julio-iglesias-3-a-247x296.jpg",
        "price": "70.00",
        "category": "Otros"
    },
    {
        "title": "Pseudo Echo - Love An Adventure",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/pseudo-echo-1a-247x296.jpg",
        "price": "130.00",
        "category": "New Wave / Post Punk"
    },
    {
        "title": "Gila - Bury My Heart At Wounded Knee",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/gila-1-a-247x296.jpg",
        "price": "140.00",
        "category": "Rock Progresivo"
    },
    {
        "title": "Wallenstein - SSSSS..Top",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/wallenstein-3a-247x296.jpg",
        "price": "120.00",
        "category": "Rock Progresivo"
    },
    {
        "title": "Lou Reed - Rock And Roll Heart*",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/Lou-Reed-Rocket-247x296.jpg",
        "price": "100.00",
        "category": "Rock"
    },
    {
        "title": "Crosby, Stills, Nash & Young - 4 Way Street",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/crosby-stills-nash-and-young-1a-247x296.jpg",
        "price": "120.00",
        "category": "Rock"
    },
    {
        "title": "UFO - No Place To Run",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/ufo-1a-247x296.jpg",
        "price": "120.00",
        "category": "Hard Rock"
    },
    {
        "title": "Gary Moore - Live",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/Gary-Moore-LiveA-247x296.jpg",
        "price": "140.00",
        "category": "Hard Rock"
    },
    {
        "title": "Cream  - Goodbye",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/cream-2a-247x296.jpg",
        "price": "170.00",
        "category": "Rock Psicodélico"
    },
    {
        "title": "The Rolling Stones - Decembers Children (And Everybodys)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/rollingstones-18-a-247x296.jpg",
        "price": "120.00",
        "category": "Rock"
    },
    {
        "title": "Sumo - Llegando Los Monos",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/sumo-llegando-247x296.jpg",
        "price": "150.00",
        "category": "Rock en Español"
    },
    {
        "title": "Soda Stereo - Canción Animal",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/sodastereo-247x296.jpg",
        "price": "150.00",
        "category": "ESENCIALES"
    },
    {
        "title": "Ray Charles - The Great Ray Charles",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/the-great-ray-charles-247x296.jpg",
        "price": "150.00",
        "category": "Soul / R & B"
    },
    {
        "title": "The Libertines - Up The Bracket",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/thelibertines-247x296.jpg",
        "price": "135.00",
        "category": "Indie Rock"
    },
    {
        "title": "Prince - Batdance",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/prince-247x296.jpg",
        "price": "130.00",
        "category": "Electrónica"
    },
    {
        "title": "Lou Reed - Transformer",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/loureed-247x296.jpg",
        "price": "200.00",
        "category": "Clásicos"
    },
    {
        "title": "Arcade Fire - The Suburbs (2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_arcadefire_thesuburbs-247x296.jpg",
        "price": "140.00",
        "category": "Indie Rock"
    },
    {
        "title": "Jimi Hendrix - Are you experienced",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/jimi-hendrix-are-you-experienced-247x296.jpg",
        "price": "150.00",
        "category": "Clásicos"
    },
    {
        "title": "Gustavo Cerati - Amor Amarillo (2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_cerati_amoramarillo-247x296.jpg",
        "price": "200.00",
        "category": "Rock en Español"
    },
    {
        "title": "Jethro Tull - Thick As A Brick (50th Anniversary Edition)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/jethro-tull-thick-as-a-brick-247x296.jpg",
        "price": "150.00",
        "category": "Rock Progresivo"
    },
    {
        "title": "Lizzo - Cuz I Love You",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/lizzo-cuz-i-love-you-247x296.jpg",
        "price": "165.00",
        "category": "Hip Hop"
    },
    {
        "title": "Pink Floyd - Dark Side of the Moon",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_pinkfloyd_darksideofthemoon-247x296.jpg",
        "price": "200.00",
        "category": "Clásicos"
    },
    {
        "title": "Deftones - White Pony (2 LP)",
        "img": "https://cdn.hatarini.com/foo/deftones-white-pony-portada-247x296.jpg",
        "price": "30.00",
        "category": "Metal"
    },
    {
        "title": "Alabama Shakes - Sound & Color (2 Lp Transparente)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/alabama-shakes-Sound-COLOR-247x296.jpg",
        "price": "125.00",
        "category": "Rock Alternativo"
    },
    {
        "title": "David Bowie - Aladdin Sane",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/David-Bowie-Aladdin-Sane-247x296.jpg",
        "price": "140.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "Judas Priest - British Steel",
        "img": "https://cdn.hatarini.com/foo/judas-priest-british-steel-247x296.jpg",
        "price": "140.00",
        "category": "Metal"
    },
    {
        "title": "Kali Uchis - Isolation",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/kali-uchis-insolation-247x296.jpg",
        "price": "150.00",
        "category": "Hip Hop"
    },
    {
        "title": "The Cure - Disintegration (2 Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/thecure-247x296.jpg",
        "price": "145.00",
        "category": "ESENCIALES"
    },
    {
        "title": "Jeff Buckley - Grace",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_jeffbuckley_grace-247x296.jpg",
        "price": "220.00",
        "category": "ESENCIALES"
    },
    {
        "title": "Shakira - Laundry Service (Yellow Vinyl)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/Shakira-Laundry-Service-247x296.jpg",
        "price": "145.00",
        "category": "Pop"
    },
    {
        "title": "Spinetta - Estrelicia MTV Unplugged",
        "img": "https://cdn.hatarini.com/foo/spinetta-mtv-unplugged-247x296.jpg",
        "price": "200.00",
        "category": "Rock en Español"
    },
    {
        "title": "Travis Scott - Birds In The Trap Sing Mcknight (2 Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/travis-scott-birds-in-the-trap-sing-mcknight-album-cover-247x296.jpg",
        "price": "200.00",
        "category": "Hip Hop"
    },
    {
        "title": "Kix - Blow My Fuse",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/DiscepSet-172653-247x296.jpg",
        "price": "200.00",
        "category": "Metal"
    },
    {
        "title": "Pink Floyd - Meddle",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/pink-floyd-meddle-247x296.jpg",
        "price": "150.00",
        "category": "Rock Progresivo"
    },
    {
        "title": "Barón Rojo - Larga Vida Al Rock And Roll",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/baron-rojo-larga-vida-247x296.jpg",
        "price": "130.00",
        "category": "Hard Rock"
    },
    {
        "title": "Michael Jackson - Bad",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/michael-jackson-bad-247x296.jpg",
        "price": "125.00",
        "category": "Pop"
    },
    {
        "title": "Miguel Mateos / Zas - Mensajes",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/discoAR-17-247x296.jpg",
        "price": "150.00",
        "category": "Rock en Español"
    },
    {
        "title": "Judas Priest - British Steel (40th Anniversary Edition)(2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/judas-priest-british-steel-247x296.jpg",
        "price": "240.00",
        "category": "Hard Rock"
    },
    {
        "title": "Guns N Roses - Appetite For Destruction",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/GUNS-247x296.jpg",
        "price": "130.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "Christian Vander, Magma - Rétrospective Vol. 1 & 2",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/CHRISTIAN-VANDER-A-247x296.jpg",
        "price": "150.00",
        "category": "Rock Progresivo"
    },
    {
        "title": "Pablo Milanés - Querido Pablo",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/QUERIDO-PABLO-A-247x296.jpg",
        "price": "120.00",
        "category": "Internacional"
    },
    {
        "title": "Irakere - Hay Mucho Que Contar",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/IRAKERE-2-A-247x296.jpg",
        "price": "100.00",
        "category": "Salsa"
    },
    {
        "title": "Los Diablos Rojos - Antologia De La Cumbia Peruana Vol. 3",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/LOS-DIABLOS-ROJOS-5A-247x296.jpg",
        "price": "120.00",
        "category": "Cumbia / Chicha"
    },
    {
        "title": "Wallenstein - Charline",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/wallenstein-1a-247x296.jpg",
        "price": "180.00",
        "category": "Rock"
    },
    {
        "title": "Picture - Traitor",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/traitor-1-a-247x296.jpg",
        "price": "130.00",
        "category": "Hard Rock"
    },
    {
        "title": "Patrick Moraz - The Story Of i",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/patrick-moraz-yes-1a-247x296.jpg",
        "price": "180.00",
        "category": "Electrónica"
    },
    {
        "title": "Miles Davis - Kind Of Blue",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/miles_davis_-_kind_of_blue_-_blue_vinyl_-_dol725hb_-_0889397006006-e1590157705152-247x296.jpg",
        "price": "150.00",
        "category": "Jazz"
    },
    {
        "title": "Soda Stereo - Soda Stereo",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/soda-stereo-soda-stereo-247x296.jpg",
        "price": "150.00",
        "category": "Rock en Español"
    },
    {
        "title": "Weezer - Weezer",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/weezer-white-album-247x296.jpg",
        "price": "160.00",
        "category": "Rock Alternativo"
    },
    {
        "title": "Nirvana - Nevermind",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_nirvana_nevermind-247x296.jpg",
        "price": "195.00",
        "category": "ESENCIALES"
    },
    {
        "title": "Hot Tuna - Live At The New Orleans House, Berkeley, California, September 1969",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/Mot-tuna-247x296.jpg",
        "price": "180.00",
        "category": "Rock"
    },
    {
        "title": "David Bowie - The Rise And Fall Of Ziggy Stardust And The Spiders From Mars",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_davidbowie_ziggystardust2-247x296.jpg",
        "price": "140.00",
        "category": "Clásicos"
    },
    {
        "title": "Green Day - Dookie",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_greenday_dookie-247x296.jpg",
        "price": "225.00",
        "category": "Rock Alternativo"
    },
    {
        "title": "Childish Gambino - Awaken, My Love!",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/childish-gambino-awaken-my-love-247x296.jpg",
        "price": "160.00",
        "category": "Hip Hop"
    },
    {
        "title": "Red Hot Chili Peppers - Unlimited Love (2 Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/red-hot-chili-peppers-unlimited-love-247x296.jpg",
        "price": "130.00",
        "category": "Rock Alternativo"
    },
    {
        "title": "The National - Sleep Well Beast (2Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/National-Sleep-Well-Beast-247x296.jpg",
        "price": "210.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "Charly Garcia - Parte De La Religion",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/charly-garcia-parte-de-la-religion-247x296.jpg",
        "price": "150.00",
        "category": "Rock en Español"
    },
    {
        "title": "Idles - Brutalism + Digital",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/idles-brutalism-247x296.jpg",
        "price": "160.00",
        "category": "Rock Alternativo"
    },
    {
        "title": "Deep Purple - Purple Passages",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/DiscepSet-183712-247x296.jpg",
        "price": "80.00",
        "category": "Rock Progresivo"
    },
    {
        "title": "Lou Reed - Berlin",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/lou-red-berlin-247x296.jpg",
        "price": "185.00",
        "category": "Vinilos Nuevos"
    },
    {
        "title": "Iron Maiden - The Book Of Souls: Live Chapter",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/iron-maiden-book-of-souls-liive-chapter-247x296.jpg",
        "price": "120.00",
        "category": "Metal"
    },
    {
        "title": "Saxon - Unplugged And Strung Up",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/saxon-unplugged-247x296.jpg",
        "price": "130.00",
        "category": "Metal"
    },
    {
        "title": "Salsa Picante - Sabrosita!",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/SALSA-PICANTE-2-A-247x296.jpg",
        "price": "110.00",
        "category": "Salsa"
    },
    {
        "title": "Spooky Tooth - Spooky Two",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/spooky-tooth-1a-247x296.jpg",
        "price": "150.00",
        "category": "Hard Rock"
    },
    {
        "title": "Fito Páez - Ciudad de Pobres Corazones",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/discoep1-9-247x296.jpg",
        "price": "110.00",
        "category": "Rock en Español"
    },
    {
        "title": "Divididos - 40 Dibujos Ahí En El Piso",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/divididos-40-dibujos-247x296.jpg",
        "price": "200.00",
        "category": "Rock Alternativo"
    },
    {
        "title": "Tame Impala - Innerspeaker (2 Lp)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/innerspeaker-247x296.jpg",
        "price": "140.00",
        "category": "Indie Rock"
    },
    {
        "title": "Neutral Milk Hotel - In The Aeroplane Over The Sea",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_neutralmilkhotel_intheaeroplaneoverthesea-247x296.jpg",
        "price": "160.00",
        "category": "Indie Rock"
    },
    {
        "title": "Little Simz - Sometimes I Might Be Introvert (Milky Vinyl)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/little-simz-sometimes-i-might-be-introvert-247x296.jpg",
        "price": "130.00",
        "category": "Hip Hop"
    },
    {
        "title": "Ramones - Rocket To Russia (Transparente)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/ramones-rocket-to-rusia-247x296.jpg",
        "price": "140.00",
        "category": "Punk"
    },
    {
        "title": "N.W.A - Straight Outta Compton",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/nwa-straight-outta-247x296.jpg",
        "price": "170.00",
        "category": "Hip Hop"
    },
    {
        "title": "The Beatles - 1",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/THE-beatles-1-247x296.jpg",
        "price": "180.00",
        "category": "Pop"
    },
    {
        "title": "Virus - Locura",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/Virus-Locura-247x296.jpg",
        "price": "360.00",
        "category": "ESENCIALES"
    },
    {
        "title": "Los Diablos Rojos - Antologia de la Cumbia Peruana Vol. 2",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/LOS-DIABLOS-ROJOS-2A-247x296.jpg",
        "price": "130.00",
        "category": "Cumbia / Chicha"
    },
    {
        "title": "Attaque 77 - El Cielo Puede Esperar",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/1rock-argentino-50-247x296.jpg",
        "price": "275.00",
        "category": "Punk"
    },
    {
        "title": "Johnny Cash - The Best Of The Johnny Cash TV Show: 1969-1971",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/johnnycash1-247x296.jpg",
        "price": "160.00",
        "category": "Clásicos"
    },
    {
        "title": "Fleetwood Mac - Greatest Hits",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/disco500px_fleetwoodmac_greatesthits-247x296.jpg",
        "price": "175.00",
        "category": "Clásicos"
    },
    {
        "title": "The White Stripes - The White Stripes",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/the-white-stripes-s-t-247x296.jpg",
        "price": "180.00",
        "category": "Blues Rock"
    },
    {
        "title": "Carole King - Her Greatest Hits (Songs Of Long Ago)",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/carole-king-her-greatest-hits-247x296.jpg",
        "price": "150.00",
        "category": "Pop"
    },
    {
        "title": "Pescado Rabioso - Lo Mejor De Pescado Rabioso",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/lo-mejor-de-pescado-rabioso-247x296.jpg",
        "price": "200.00",
        "category": "Rock en Español"
    },
    {
        "title": "Mac Demarco - Another One",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/mac-the-marco-another-one-247x296.jpg",
        "price": "200.00",
        "category": "Indie Rock"
    },
    {
        "title": "David Bowie Narrates Prokofiev* / Peter And The Wolf",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/DAVID-BOWIE-1-A-247x296.jpg",
        "price": "80.00",
        "category": "Otros"
    },
    {
        "title": "Manu Chao - Clandestino",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/manu-chao-clandestino-247x296.jpg",
        "price": "150.00",
        "category": "Reggae"
    },
    {
        "title": "A$AP Rocky - Long.Live.A$AP",
        "img": "https://s3.amazonaws.com/cdn.hatarini.com/foo/aap-rocky-long-live-aap-247x296.jpg",
        "price": "165.00",
        "category": "Hip Hop"
    }
])

const detail = ref({} as any)

const doFilter = (category:string)=>{
    data.value = data.value.filter(d=>d.category===category)
}

const categoryClass = (category:string)=>{
    const itIncludes = (subCategory:string)=>{
        return category.toLowerCase().includes(subCategory.toLowerCase())
    }
    switch(true){
        case itIncludes('Rock'): return 'text-teal-700 bg-cyan-300'
        case itIncludes('Pop'): return 'text-teal-700 bg-yellow'
        case itIncludes('Hip Hop'): return 'text-yellow bg-red-700'
        case itIncludes('Soul'): return 'text-info bg-white'
        case itIncludes('Elect'): return 'bg-purple-600'
        case itIncludes('Reggae'): return 'text-info bg-green-500'
        case itIncludes('Clásicos'): return 'text-info bg-pink-500'
        case itIncludes('Salsa'): return 'text-info bg-red-500'
        default: return 'text-info bg-gray'
    }
}

const showDetail = (item:any)=>{
    detail.value = item
}

</script>
<template>
<div grid4 gap-4 m-16>
    <div v-for="d in data" 
    bg-gray-500 p-8 col center
    text-xs
    >
    <div p-4 backdrop-blur-lg col center gap-4 w-64 rounded-xl shadow-info sh-md
        v-if="d===detail"
    >
       <h2 p-1 text-center text-xs>{{d.title}}</h2>
        <h3 p-2 rounded font-extrabold text-sm w-fit shadow text-info
        @click="doFilter(d.category)"
        :class="categoryClass(d.category)"
        ><strong>{{d.category}}</strong></h3>
        <span>S/.{{d.price}}</span>
        <Ico icon="mdi-cart" rf/>
    </div>    
    <div m-4 hover:animate-spin cp class="bg-gradient-to-r from-gray-700 via-gray-900 to-black" p-8 rf >
    
        <div :style="{backgroundImage: 'url('+d.img+')'}" class="bg-fit bg-center bg-no-repeat w-32 h-32 rounded-full shadow-info sh-md"
        @click="showDetail(d)"
        ></div>
    
    </div>
        </div>
    </div>
</template>