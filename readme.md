<!--lint disable awesome-heading-->
# Awesome Discord.py [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<p align="center">
  <a href="https://discordpy.readthedocs.io/en/stable/">
    <img src="assets/banner.png" width="792" alt="discord.py">
  </a>
</p>

> Useful resources for creating Discord bots with [discord.py](https://discordpy.readthedocs.io/en/stable/).

discord.py is a modern, easy to use, feature-rich, and async-ready API wrapper for Discord.

## Contents

- [Official Links](#official-links)
- [Libraries and Extensions](#libraries-and-extensions)
- [Example Bots](#example-bots)
- [Blog Posts, Guides and Tutorials](#blog-posts-guides-and-tutorials)
- [Community Gists and Snippets](#community-gists-and-snippets)
- [Additional Resources](#additional-resources)
- [Forks and Wrappers](#forks-and-wrappers)
- [Related](#related)

<!-- CONTENT -->

## Official Links

- [Discord.py Documentation](https://discordpy.readthedocs.io/en/latest/) - API reference, guides, and examples.
- [Discord.py Changelog](https://discordpy.readthedocs.io/en/latest/whats_new.html) - Release notes and breaking changes.
- [Discord.py FAQ](https://discordpy.readthedocs.io/en/latest/faq.html) - Common questions and answers.
- [Migrating to v2.0](https://discordpy.readthedocs.io/en/latest/migrating.html) - Breaking-change guide for 2.0.
- [Discord.py Quickstart](https://discordpy.readthedocs.io/en/latest/quickstart.html) - Minimal getting-started example.
- [Discord.py Discord Server](https://discord.gg/dpy) - Official community Discord.
- [Official Examples](https://github.com/Rapptz/discord.py/tree/master/examples) - Example bots and snippets from the upstream repo. <sup><i>last activity 2026-09</i></sup>
- [Discord.py GitHub](https://github.com/Rapptz/discord.py) - Upstream source repository. <sup><i>last activity 2026-09</i></sup>

## Libraries and Extensions

### Utilities

- [Kyrela/discore](https://github.com/Kyrela/discore) - Bot bootstrap with log and error tracking. <sup><i>last activity 2026-10</i></sup>
- [tibue99/ezcord](https://github.com/tibue99/ezcord) - Cogs, i18n, error webhooks, and embed helpers; also works with Pycord. <sup><i>last activity 2026-10</i></sup>
- [Soheab/discord-ext-subcommands](https://github.com/Soheab/discord-ext-subcommands) - Define prefix, slash, and hybrid subcommands across files and cogs. <sup><i>last activity 2026-09</i></sup>
- [python-discord/bot-core](https://github.com/python-discord/bot-core) - Shared utilities used by Python Discord's bots. <sup><i>last activity 2026-09</i></sup>
- [clari7744/DPyUtils](https://github.com/clari7744/DPyUtils) - Duration parsing, extra converters, and a context editor that re-runs commands when the user edits their message. <sup><i>last activity 2026-04</i></sup>
- [mikeshardmind/discord-scheduler](https://github.com/mikeshardmind/discord-scheduler) - Persistent SQLite-backed task scheduler with timezone-aware wall times. <sup><i>last activity 2025-02</i></sup>
- [Soheab/discord-ext-custom_interaction](https://github.com/Soheab/discord-ext-custom_interaction) - Subclass `discord.Interaction` with helpers such as `send` and `author`. <sup><i>last activity 2025-01</i></sup>
- [InterStella0/starlight-dpy](https://github.com/InterStella0/starlight-dpy) - Paginated help commands, inline views, and converters. Pre-alpha; not for production. <sup><i>last activity 2024-02</i></sup>
- [Voxel-Fox-Ltd/VoxelBotUtils](https://github.com/Voxel-Fox-Ltd/VoxelBotUtils) - Config, database, logging, error handling, and help-command helpers, built for Novus. <sup><i>last activity 2024-01</i></sup>
- [Soheab/discord.py-listen-overloads](https://github.com/Soheab/discord.py-listen-overloads) - Type stubs that add overloads to `@commands.Bot.listen` for library events. <sup><i>last activity 2023-12</i></sup>
- [timelessnesses/dpyhr](https://github.com/timelessnesses/dpyhr) - Reloads cogs on save using the built-in cog loader. <sup><i>last activity 2023-04</i></sup>
- [tanrbobanr/dpy-check](https://github.com/tanrbobanr/dpy-check) - Composable, dynamic checks for prefix and application commands. <sup><i>last activity 2023-01</i></sup>

### Testing and Debugging

- [python-discord/snekbox](https://github.com/python-discord/snekbox) - NSJail sandbox for evaluating untrusted Python, used by Python Discord. <sup><i>last activity 2026-10</i></sup>
- [CraftSpider/dpytest](https://github.com/CraftSpider/dpytest) - Fake Discord backend for writing bot tests. <sup><i>last activity 2026-06</i></sup>
- [scarletcafe/jishaku](https://github.com/scarletcafe/jishaku) - REPL, extension reload, and debug cog for running bots. <sup><i>last activity 2026-04</i></sup>

### UI

- [thegamecracks/discord-ext-pager](https://github.com/thegamecracks/discord-ext-pager) - Paginator with an API close to discord-ext-menus. <sup><i>last activity 2026-10</i></sup>
- [keizaiya/discord-ext-flow](https://github.com/keizaiya/discord-ext-flow) - State-machine control flow on top of `discord.ui`. <sup><i>last activity 2026-10</i></sup>
- [HollowTheSilver/CascadeUI](https://github.com/HollowTheSilver/CascadeUI) - Redux-style centralized state, persistence, and Components V2 patterns. <sup><i>last activity 2026-10</i></sup>
- [Defxult/reactionmenu](https://github.com/Defxult/reactionmenu) - Paginator with buttons, reactions, and select-based categories. <sup><i>last activity 2026-05</i></sup>
- [Soheab/discord-py-paginators](https://github.com/Soheab/discord-py-paginators) - Button and other paginator types with published docs. <sup><i>last activity 2025-10</i></sup>
- [Soheab/cv2examples](https://github.com/Soheab/cv2examples) - Screenshots and sample layouts for Components V2. <sup><i>last activity 2025-07</i></sup>
- [Soheab/modal-paginator](https://github.com/Soheab/modal-paginator) - Paginate a Modal across pages using buttons. <sup><i>last activity 2025-05</i></sup>
- [philskillz-coder/discord-py-paginator](https://github.com/philskillz-coder/discord-py-paginator) - View-based embed paginator. <sup><i>last activity 2025-04</i></sup>
- [Soheab/discord-ext-embeds](https://github.com/Soheab/discord-ext-embeds) - Embed constructor with author/footer shortcuts, file media, and character-limit checks. <sup><i>last activity 2025-03</i></sup>
- [OnceYT/dpy-paginator](https://github.com/OnceYT/dpy-paginator) - Dependency-free embed paginator. <sup><i>last activity 2024-10</i></sup>
- [sizumita/discord-ext-ui](https://github.com/sizumita/discord-ext-ui) - Declarative SwiftUI-style views with reactive state; works with Pycord too. <sup><i>last activity 2024-10</i></sup>
- [Modern-Realm/discord_btns_menus](https://github.com/Modern-Realm/discord_btns_menus) - Buttons, select menus, combinations, and pagination; also supports related forks. <sup><i>last activity 2024-06</i></sup>
- [LiBa001/disputils](https://github.com/LiBa001/disputils) - Pagination, confirmation dialogs, and small UI helpers. <sup><i>last activity 2024-05</i></sup>
- [vcv88/discord-ext-dyn](https://github.com/vcv88/discord-ext-dyn) - Dynamic creation of modals, buttons, and select menus. <sup><i>last activity 2024-01</i></sup>
- [Seniatical/dpy-paginator](https://github.com/Seniatical/dpy-paginator) - Button and dropdown pagination. <sup><i>last activity 2023-04</i></sup>

### Inter-Process Communication

- [No767/discord-ext-ipcx](https://github.com/No767/discord-ext-ipcx) - Maintained IPC extension for splitting the bot across processes. <sup><i>last activity 2026-10</i></sup>

### Voice receive

- [discord-ext-voice-recv](https://github.com/imayhaveborkedit/discord-ext-voice-recv) - Receive and process users' voice packets. <sup><i>last activity 2025-06</i></sup>
- [Sheppsu/discord-ext-listening](https://github.com/Sheppsu/discord-ext-listening) - Voice receive via multiprocessing. <sup><i>last activity 2024-02</i></sup>

### Voice send

- [tuna2134/discord-ext-songbird](https://github.com/tuna2134/discord-ext-songbird) - Rust Songbird voice client wrapper; Linux and macOS only. <sup><i>last activity 2026-10</i></sup>

### Lavalink

- [devoxin/Lavalink.py](https://github.com/devoxin/Lavalink.py) - Lavalink client with multi-node load balancing, filters, and custom sources. <sup><i>last activity 2026-10</i></sup>
- [cloudwithax/pomice](https://github.com/cloudwithax/pomice) - Lavalink client with Spotify and Apple Music querying. <sup><i>last activity 2026-10</i></sup>
- [ooliver1/mafic](https://github.com/ooliver1/mafic) - Typed Lavalink client that also supports nextcord, disnake, and Pycord. <sup><i>last activity 2026-10</i></sup>
- [PyLav/PyLav](https://github.com/PyLav/PyLav) - Lavalink wrapper aimed at bots including Red-DiscordBot. <sup><i>last activity 2026-10</i></sup>
- [sonolink/sonolink](https://github.com/sonolink/sonolink) - Typed Lavalink v4 client built on msgspec; also supports Pycord and disnake. <sup><i>last activity 2026-10</i></sup>
- [ParrotXray/lava-lyra](https://github.com/ParrotXray/lava-lyra) - Lavalink v4 and Nodelink v3 client that also supports Pycord. <sup><i>last activity 2026-08</i></sup>
- [PythonistaGuild/Wavelink](https://github.com/PythonistaGuild/Wavelink) - Async Lavalink v4 client. <sup><i>last activity 2026-07</i></sup>
- [HazemMeqdad/lavaplay.py](https://github.com/HazemMeqdad/lavaplay.py) - Lavalink v4 node manager that works with any async Discord wrapper. <sup><i>last activity 2026-05</i></sup>
- [Cog-Creators/Red-Lavalink](https://github.com/Cog-Creators/Red-Lavalink) - Lavalink client used by Red-DiscordBot, usable in any bot. <sup><i>last activity 2026-03</i></sup>

### Authentication

- [Soheab/oauthcord.py](https://github.com/Soheab/oauthcord.py) - Async OAuth2 client with typed REST models; not a bot framework. <sup><i>last activity 2026-10</i></sup>
- [Rapptz/open-collective-discord-auth](https://github.com/Rapptz/open-collective-discord-auth) - Linked-role auth server for Open Collective membership. <sup><i>last activity 2026-06</i></sup>
- [treeben77/discord-oauth2.py](https://github.com/treeben77/discord-oauth2.py) - OAuth2 and Linked Roles REST wrapper. <sup><i>last activity 2026-01</i></sup>

### Metrics, Monitoring, and Logging

- [EthanC/Loguru-Discord](https://github.com/EthanC/Loguru-Discord) - Loguru sink that posts logs to a webhook. <sup><i>last activity 2026-10</i></sup>
- [discord-ext-prometheus](https://github.com/ApolloRoboto/discord.py-ext-prometheus) - Prometheus metrics exporter for running bots. <sup><i>last activity 2025-02</i></sup>
- [python-discord/metricity](https://github.com/python-discord/metricity) - Metric collection used on the Python Discord server. <sup><i>last activity 2024-09</i></sup>

### Miscellaneous

- [Skelmis/Discord-Anti-Spam](https://github.com/Skelmis/Discord-Anti-Spam) - Automatic spam handling for commands and messages. <sup><i>last activity 2026-07</i></sup>
- [mahtoid/DiscordChatExporterPy](https://github.com/mahtoid/DiscordChatExporterPy) - Export channel history to HTML transcripts. <sup><i>last activity 2026-05</i></sup>
- [Tom-the-Bomb/Discord-Games](https://github.com/Tom-the-Bomb/Discord-Games) - Drop-in games such as chess, Connect Four, hangman, and 2048, played through reactions or buttons. <sup><i>last activity 2026-03</i></sup>
- [YousefEZ/discord-qalib](https://github.com/YousefEZ/discord-qalib) - XML templates for embeds and paginated menus. <sup><i>last activity 2026-01</i></sup>
- [Bluenix2/discord-typings](https://github.com/Bluenix2/discord-typings) - TypedDicts for Discord gateway and HTTP payloads. <sup><i>last activity 2025-04</i></sup>
- [CasuallyCalm/discord-pretty-help](https://github.com/CasuallyCalm/discord-pretty-help) - Embed-based replacement for the built-in help command. <sup><i>last activity 2023-07</i></sup>

### Templates

- [kkrypt0nn/Python-Discord-Bot-Template](https://github.com/kkrypt0nn/Python-Discord-Bot-Template) - Starter project for a personalized bot. <sup><i>last activity 2026-10</i></sup>
- [PaulMarisOUMary/Discord-Bot](https://github.com/PaulMarisOUMary/Discord-Bot) - 2.x starter with hybrid commands, Docker, logging, and a database. <sup><i>last activity 2026-10</i></sup>

## Example Bots

### Reference implementations

- [AlexFlipnote/discord_bot.py](https://github.com/AlexFlipnote/discord_bot.py) - Minimal starter bot. <sup><i>last activity 2026-10</i></sup>
- [avizum/alpine](https://github.com/avizum/alpine) - Public source for a general-purpose bot; author recommends the hosted instance. <sup><i>last activity 2026-10</i></sup>
- [AbstractUmbra/Mipha](https://github.com/AbstractUmbra/Mipha) - Umbra's personal bot, forked from RoboDanny and kept on latest library releases. <sup><i>last activity 2026-10</i></sup>
- [Kile/Killua](https://github.com/Kile/Killua) - Games, moderation, and todo lists, plus extra algorithm notes in-tree. <sup><i>last activity 2026-08</i></sup>
- [Rapptz/RoboDanny](https://github.com/Rapptz/RoboDanny) - Rapptz's production bot; commonly used as a reference implementation. <sup><i>last activity 2026-06</i></sup>
- [onerandomusername/monty-python](https://github.com/onerandomusername/monty-python) - Helper bot for Python project development. <sup><i>last activity 2026-02</i></sup>

### Community and moderation

- [python-discord/bot](https://github.com/python-discord/bot) - Moderation, utils, and community tools for Python Discord. <sup><i>last activity 2026-10</i></sup>
- [modmail-dev/Modmail](https://github.com/modmail-dev/Modmail) - Shared staff inbox, similar to Reddit Modmail. <sup><i>last activity 2026-10</i></sup>
- [python-discord/sir-lancebot](https://github.com/python-discord/sir-lancebot) - On-ramp bot for new open-source contributors at Python Discord. <sup><i>last activity 2026-09</i></sup>
- [Tortoise-Community/tortoise-bot](https://github.com/Tortoise-Community/tortoise-bot) - Community bot for the Tortoise Discord. <sup><i>last activity 2026-09</i></sup>
- [python-discord/sir-robin](https://github.com/python-discord/sir-robin) - Event-management bot for Python Discord. <sup><i>last activity 2026-08</i></sup>
- [fourjr/rainbot](https://github.com/fourjr/rainbot) - Moderation bot with automod and logging. <sup><i>last activity 2026-04</i></sup>
- [PythonistaGuild/Pythonista-Bot](https://github.com/PythonistaGuild/Pythonista-Bot) - Guild bot for the Pythonista Guild server. <sup><i>last activity 2025-02</i></sup>
- [DeJayDev/speedboat](https://github.com/DeJayDev/speedboat) - Tools for running large community servers. <sup><i>last activity 2024-09</i></sup>

### Frameworks

- [Cog-Creators/Red-DiscordBot](https://github.com/Cog-Creators/Red-DiscordBot) - Self-hosted modular bot with a large cog ecosystem. <sup><i>last activity 2026-10</i></sup>

### Music and games

- [ChocoMeow/Vocard](https://github.com/ChocoMeow/Vocard) - Music bot for YouTube, SoundCloud, Spotify, and Twitch. <sup><i>last activity 2026-10</i></sup>
- [Ballsdex-Team/BallsDex-DiscordBot](https://github.com/Ballsdex-Team/BallsDex-DiscordBot) - Collect and trade countryballs. <sup><i>last activity 2026-10</i></sup>
- [statch/gitbot](https://github.com/statch/gitbot) - GitHub notifications and developer tools. <sup><i>last activity 2026-10</i></sup>
- [Hunter87ff/Spruce](https://github.com/Hunter87ff/Spruce) - Tournament and server management. <sup><i>last activity 2026-10</i></sup>
- [seriaati/hoyo-buddy](https://github.com/seriaati/hoyo-buddy) - User-installable bot for Genshin Impact, Honkai: Star Rail, and other Hoyoverse games. <sup><i>last activity 2026-10</i></sup>
- [Yuuzi261/Tweetcord](https://github.com/Yuuzi261/Tweetcord) - Posts new tweets from followed X/Twitter accounts to chosen channels. <sup><i>last activity 2026-10</i></sup>
- [mikeywhiston/ERM](https://github.com/mikeywhiston/ERM) - Staff tools aimed at Roblox communities. <sup><i>last activity 2026-09</i></sup>
- [jakobdylanc/llmcord](https://github.com/jakobdylanc/llmcord) - LLM frontend for OpenAI-compatible APIs. <sup><i>last activity 2026-08</i></sup>
- [cheran-senthil/TLE](https://github.com/cheran-senthil/TLE) - Competitive programming helper for Codeforces and similar sites. <sup><i>last activity 2026-03</i></sup>
- [poketwo/poketwo](https://github.com/poketwo/poketwo) - Pokémon catching and collecting, in the Pokécord style. <sup><i>last activity 2025-02</i></sup>

### Multipurpose

- [joinemm/miso-bot](https://github.com/joinemm/miso-bot) - General-purpose bot with Last.fm and K-pop commands. <sup><i>last activity 2026-10</i></sup>
- [Axobot-org/Axobot](https://github.com/Axobot-org/Axobot) - Multilingual general-purpose bot with moderation, XP, and Minecraft lookups. <sup><i>last activity 2026-10</i></sup>
- [Iapetus-11/Villager-Bot](https://github.com/Iapetus-11/Villager-Bot) - Minecraft-themed bot with server status checks, pixel art, and an economy game; sharded across clusters. <sup><i>last activity 2026-10</i></sup>
- [wasi-master/wm_bot](https://github.com/wasi-master/wm_bot) - General-purpose bot with a large command set. <sup><i>last activity 2026-07</i></sup>
- [DTS-11/PizzaHat](https://github.com/DTS-11/PizzaHat) - General-purpose bot with a public website and AGPL source. <sup><i>last activity 2026-05</i></sup>
- [Nirlep5252/EpicBot](https://github.com/Nirlep5252/EpicBot) - General-purpose bot with a large public command set. <sup><i>last activity 2025-07</i></sup>

## Blog Posts, Guides and Tutorials

- [User Installable Applications - Umbra's Rantings](https://about.abstractumbra.dev/discord.py/2024/04/11/user-installable-applications.html) - Installable app commands and how to register them.
- [All about selects - Umbra's Rantings](https://about.abstractumbra.dev/discord.py/2023/09/25/selects.html) - Select menu types and how to use them.
- [Application Command definition examples - Umbra's Rantings](https://about.abstractumbra.dev/discord.py/2023/01/30/app-command-examples.html) - Examples of slash, user, and message command definitions.
- [Application command basics - Umbra's Rantings](https://about.abstractumbra.dev/discord.py/2023/01/30/app-command-basics.html) - Slash commands through modals and other components.
- [Umbra's Sync Command - Umbra's Rantings](https://about.abstractumbra.dev/discord.py/2023/01/29/sync-command-example.html) - CommandTree sync command and how it works.
- [Discord.py Masterclass](https://fallendeity.github.io/discord.py-masterclass/) - From-scratch tutorial covering library features.
- [Python Discord - Discord.py Learning Guide](https://www.pythondiscord.com/pages/guides/python-guides/discordpy/) - Curated learning path for setup, commands, and FAQ.
- [Components V2 - Umbra's Rantings](https://about.abstractumbra.dev/discord.py/2025/08/17/components-v2.html) - LayoutView and Discord's Components V2 in library 2.6.

## Community Gists and Snippets

### Help Commands

- [voidoak/Implementing Help](https://gist.github.com/voidoak/4f34922888eeca04e1bba8c0ebd2f948) - Tutorial on implementing your own help command. <sup><i>last activity 2026-03</i></sup>
- [InterStella0/HelpCommand walkthrough](https://gist.github.com/InterStella0/b78488fb28cadf279dfd3164b9f0cf96) - Walkthrough for subclassing HelpCommand. <sup><i>last activity 2025-12</i></sup>
- [nonchris/Custom Help Command](https://gist.github.com/nonchris/1c7060a14a9d94e7929aa2ef14c41bc2) - Advanced custom help command example. <sup><i>last activity 2024-08</i></sup>
- [Rapptz/Embed Help Command](https://gist.github.com/Rapptz/31a346ed1eb545ddeb0d451d81a60b3b) - Embed-based help command example from the library author. <sup><i>last activity 2024-07</i></sup>
- [Gobot1234/Sub-classing Help](https://gist.github.com/Gobot1234/45cad24df63fc144e85a7f8c85812567) - Guide to subclassing the help command. <sup><i>last activity 2021-07</i></sup>

### Error Handling

- [EvieePy/Error Handling](https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612) - Error handling for prefix and app commands. <sup><i>last activity 2026-10</i></sup>
- [irregularunit/Command Error Handler](https://gist.github.com/irregularunit/0221164777a476c653e36b49439b7b06) - Structured command error handler example. <sup><i>last activity 2023-07</i></sup>
- [Jeftaei/AppCommandErrorhandler.py](https://gist.github.com/Jeftaei/d0bad5044f1192a4c454f95a6b591d53) - Error handler covering prefix and app commands. <sup><i>last activity 2023-05</i></sup>

### Components and UI

- [Soheab/Simple Button Paginator](https://gist.github.com/Soheab/f226fc06a3468af01ea3168c95b30af8) - Small paginator with three buttons. <sup><i>last activity 2026-04</i></sup>
- [Soheab/Global View](https://gist.github.com/Soheab/cfd769870b7b6eaf00a7aebf5293a622) - Pattern for a globally registered view. <sup><i>last activity 2026-04</i></sup>
- [lykn/Buttons](https://gist.github.com/lykn/bac99b06d45ff8eed34c2220d86b6bf4) - How to make buttons in v2. <sup><i>last activity 2026-02</i></sup>
- [lykn/Selects or Dropdowns](https://gist.github.com/lykn/a2b68cb790d6dad8ecff75b2aa450f23) - Select menus in v2. <sup><i>last activity 2026-01</i></sup>
- [InterStella0/Pagination Walkthrough](https://gist.github.com/InterStella0/454cc51e05e60e63b81ea2e8490ef140) - Walkthrough of action-based pagination. <sup><i>last activity 2025-04</i></sup>
- [imptype/Message Maker](https://gist.github.com/imptype/7b35c6769684fb68178e5719e5f81b6d) - Embed/message builder command. <sup><i>last activity 2025-03</i></sup>
- [esmaycat/Message Components](https://gist.github.com/esmaycat/500eafdad0aaf278b94c612764688976) - Using message components in 2.0. <sup><i>last activity 2025-02</i></sup>
- [Soheab/wait_for Modal](https://gist.github.com/Soheab/f46fee27498aad4a8962d59b6f0415c6) - Wait for user input with a modal. <sup><i>last activity 2024-11</i></sup>
- [mikeshardmind/List Menu](https://gist.github.com/mikeshardmind/bff6f937032455d83b8f1724ef73575a) - List menu pagination snippet. <sup><i>last activity 2024-03</i></sup>
- [quackbarc/2.0 Paginators](https://gist.github.com/quackbarc/31e5cd789d232ad0d263511bb1a506e8) - Paginator examples for 2.0. <sup><i>last activity 2022-03</i></sup>

### Components V2

- [Soheab/Components V2 to LayoutView](https://gist.github.com/Soheab/ab7a833725f95a84a8f7fa17995cb36c) - Mapping Components V2 to LayoutView. <sup><i>last activity 2026-07</i></sup>
- [Soheab/CV2 Paginator](https://gist.github.com/Soheab/891c39d7294b1bdbadc7ecf35ce51cc5) - Components V2 paginator. <sup><i>last activity 2026-04</i></sup>
- [Soheab/Embed to Container](https://gist.github.com/Soheab/cf356c62a6134508869bf40640b04856) - Convert an embed into a Components V2 container. <sup><i>last activity 2025-11</i></sup>

### Cogs and Commands

- [Soheab/self.bot in Cogs](https://gist.github.com/Soheab/cf387b753da32eb02f3228c2e32bb03f) - How `self.bot` works inside a cog. <sup><i>last activity 2026-08</i></sup>
- [EvieePy/Cogs Example](https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be) - Classic cogs and extension layout. <sup><i>last activity 2025-08</i></sup>
- [Soheab/wait_for in Commands](https://gist.github.com/Soheab/e73ab6f66881ee4102be37815da3a24e) - Examples of `wait_for` inside ext.commands. <sup><i>last activity 2025-06</i></sup>
- [LeoCx1000/MentionableTree implementation](https://gist.github.com/LeoCx1000/021dc52981299b95ea7790416e4f5ca4) - Mentionable CommandTree so slash commands can be mentioned. <sup><i>last activity 2025-05</i></sup>
- [Painezor/Checks](https://gist.github.com/Painezor/eb2519022cd2c907b56624105f94b190) - Built-in checks for the commands extension. <sup><i>last activity 2025-04</i></sup>
- [Samarthh2601/App Commands Walkthrough](https://gist.github.com/Samarthh2601/b6f57065f394b54f43666037ade38d32) - Walkthrough for application commands. <sup><i>last activity 2025-01</i></sup>
- [Soheab/Any-Permission Check](https://gist.github.com/Soheab/ec3f40f9f54add0dba787783719331f8) - Custom check that passes if the user has any of the given permissions. <sup><i>last activity 2024-07</i></sup>
- [Ikusaba-san/Cog Methods](https://gist.github.com/Ikusaba-san/69115b79d33e05ed07ec4a4f14db83b1) - List of special cog methods. <sup><i>last activity 2021-05</i></sup>

### Other Snippets

- [kkrypt0nn/ANSI Colors on Discord](https://gist.github.com/kkrypt0nn/a02506f3712ff2d1c8ca7c9e0aed7c06) - ANSI color codes in Discord code blocks. <sup><i>last activity 2026-10</i></sup>
- [LeviSnoot/Discord Timestamps](https://gist.github.com/LeviSnoot/d9147767abeef2f770e9ddcd91eb85aa) - Discord timestamp markdown syntax. <sup><i>last activity 2026-10</i></sup>
- [advaith1/Intents Explainer](https://gist.github.com/advaith1/e69bcc1cdd6d0087322734451f15aa2f) - Gateway and privileged intents: statuses, members, and message content. <sup><i>last activity 2026-09</i></sup>
- [mikeshardmind/SQLite Examples](https://gist.github.com/mikeshardmind/d7d2c6cb19b53ab76b7d401b2716df5d) - Common SQLite patterns for bots. <sup><i>last activity 2026-09</i></sup>
- [Soheab/APIs for Discord Bots](https://gist.github.com/Soheab/332ba85f8989648449c71bdc8ef32368) - Community list of APIs commonly used with Discord bots. <sup><i>last activity 2026-08</i></sup>
- [Soheab/Threads](https://gist.github.com/Soheab/4709e335474784d8a1877812f6d0c354) - Creating and managing Discord threads. <sup><i>last activity 2026-07</i></sup>
- [4Kaylum/Discord.py Tutorial](https://gist.github.com/4Kaylum/a1e9f31c31b17386c36f017d3c59cdcc) - Simple bot tutorial. <sup><i>last activity 2026-05</i></sup>
- [AkshuAgarwal/Interactions](https://gist.github.com/AkshuAgarwal/bc7d45bcecd5d29de4d6d7904e8b8bd8) - Intro to interactions and how to handle them. <sup><i>last activity 2026-02</i></sup>
- [Soheab/Voice Channel Status](https://gist.github.com/Soheab/e9a747f5c8fae43447a5611e483b4beb) - React when a voice channel status is set or changed. <sup><i>last activity 2026-02</i></sup>
- [Soheab/discord.Colour](https://gist.github.com/Soheab/d9cf3f40e34037cfa544f464fc7d919e) - Reference for discord.Colour helpers. <sup><i>last activity 2026-02</i></sup>
- [scragly/Learning discord.py](https://gist.github.com/scragly/095b5278a354d46e86f02d643fc3d64b) - Setup, core concepts, and a resource list for learning the library. <sup><i>last activity 2025-12</i></sup>
- [Soheab/No Message Content Intent Ideas](https://gist.github.com/Soheab/a6229dbbe3acf3ce9a4625bf9e7177da) - Command ideas that work without the privileged message content intent. <sup><i>last activity 2025-12</i></sup>
- [cibere/Defer Response](https://gist.github.com/cibere/7e1356575780e716d2e3a23ea2bcf6da) - Acknowledge an interaction and respond later, up to 15 minutes. <sup><i>last activity 2025-02</i></sup>
- [Soheab/Server Tag](https://gist.github.com/Soheab/d5e7fdbca3db94629cf87f1178096aab) - Overflow copy of a long official-server tag that exceeded Discord's character limit. <sup><i>last activity 2024-10</i></sup>
- [philskillz-coder/Color Transformer](https://gist.github.com/philskillz-coder/c6bee6c8e258ad56afb01840df26a1fa) - Color transformer and autocomplete. <sup><i>last activity 2023-06</i></sup>
- [CuteFwan/wait_for Multiple Events](https://gist.github.com/CuteFwan/ded1bf520d71baac18726fa2e0554f0f) - Waiting for more than one Discord event at a time. <sup><i>last activity 2021-08</i></sup>

## Additional Resources

- [Permissions Calculator](https://discordapi.com/permissions.html) - Build bot invite links with a chosen permission bitfield.
- [Discord Community Resources](https://discord.com/developers/docs/topics/community-resources) - Official index of libraries, calculators, and embed tools.
- [Intent Calculator](https://ziad87.net/intents/) - Build a gateway intents bitfield for Identify.
- [Embed Visualizer](https://leovoel.github.io/embed-visualizer/) - Live embed designer with generated library snippets.
- [scarletcafe/discord.py-docker](https://github.com/scarletcafe/discord.py-docker) - Source for the `gorialis/discord.py` Docker images with the library preinstalled. <sup><i>last activity 2026-04</i></sup>
- [Soheab/discord.py-tags](https://github.com/Soheab/discord.py-tags) - Overflow copies of long tags from the official library Discord. <sup><i>last activity 2024-12</i></sup>
- [Soheab/dpy-badhosts](https://github.com/Soheab/dpy-badhosts) - Hosts the community generally warns against using for bots. <sup><i>last activity 2024-11</i></sup>
- [Soheab/dpy-missing-features](https://github.com/Soheab/dpy-missing-features) - Discord API features the library does not yet expose. <sup><i>last activity 2024-08</i></sup>
- [Rapptz/asqlite](https://github.com/Rapptz/asqlite) - Async wrapper around sqlite3. <sup><i>last activity 2024-07</i></sup>
- [discord-interactions-python](https://github.com/discord/discord-interactions-python) - Official helpers for verifying HTTP interaction signatures. <sup><i>last activity 2024-04</i></sup>

## Forks and Wrappers

disnake, nextcord, Novus, pycord, and discord.py-message-components are discord.py forks. hikari, hata, interactions.py, and discord.http are independent wrappers, not drop-in replacements for discord.py.

- [disnake](https://github.com/DisnakeDev/disnake) - Async Discord API wrapper, forked from discord.py. <sup><i>last activity 2026-10</i></sup>
- [nextcord](https://github.com/nextcord/nextcord) - API wrapper forked from discord.py. <sup><i>last activity 2026-10</i></sup>
- [pycord](https://github.com/Pycord-Development/pycord) - Maintained fork of discord.py. <sup><i>last activity 2026-10</i></sup>
- [hikari](https://github.com/hikari-py/hikari) - Independent async wrapper, not a drop-in replacement. <sup><i>last activity 2026-10</i></sup>
- [interactions.py](https://github.com/interactions-py/interactions.py) - Independent bot framework, not a drop-in replacement. <sup><i>last activity 2026-10</i></sup>
- [hata](https://github.com/HuyaneMatsu/hata) - Independent async wrapper, not a drop-in replacement. <sup><i>last activity 2026-10</i></sup>
- [AlexFlipnote/discord.http](https://github.com/AlexFlipnote/discord.http) - HTTP-interactions-first library with optional gateway and cache control. <sup><i>last activity 2026-10</i></sup>
- [Novus](https://github.com/Voxel-Fox-Ltd/Novus) - Async API wrapper forked from discord.py, used by VoxelBotUtils. <sup><i>last activity 2026-07</i></sup>
- [mccoderpy/discord.py-message-components](https://github.com/mccoderpy/discord.py-message-components) - Fork that added message components before they landed upstream. <sup><i>last activity 2025-06</i></sup>

## Related

- [Discord Library Comparison](https://libs.advaith.io) - Feature matrix across Discord libraries.
- [jacc/awesome-discord](https://github.com/jacc/awesome-discord) - Clients, bots, libraries, and related tools. <sup><i>last activity 2026-05</i></sup>
- [awesome-discord-communities](https://github.com/mhxion/awesome-discord-communities) - Programmer Discord communities. <sup><i>last activity 2026-04</i></sup><!-- END CONTENT -->

## Contributing

[Contributions of any kind welcome, just follow the guidelines](contributing.md)!

### Contributors

[Thanks goes to these contributors](https://github.com/kzndotsh/awesome-discordpy/graphs/contributors)!
