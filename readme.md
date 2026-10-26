<!--lint disable awesome-heading-->
# Awesome Discord.py [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<p align="center">
  <a href="https://discordpy.readthedocs.io/en/stable/">
    <img src="assets/banner.png" width="792" alt="discord.py">
  </a>
</p>

> Useful resources for creating Discord bots with [discord.py](https://discordpy.readthedocs.io/en/stable/).

discord.py is a modern, easy to use, feature-rich, and async-ready API wrapper for Discord.

Last Activity: ⚡ within 6 months · 🕰️ 6–24 months · 💤 over 2 years. Hover an icon for the month.

## Contents

- [Official Links](#official-links)
- [Libraries and Extensions](#libraries-and-extensions)
  - [Utilities](#utilities)
  - [Testing and Debugging](#testing-and-debugging)
  - [UI](#ui)
  - [Inter-Process Communication](#inter-process-communication)
  - [Voice receive](#voice-receive)
  - [Voice send](#voice-send)
  - [Lavalink](#lavalink)
  - [Authentication](#authentication)
  - [Metrics, Monitoring, and Logging](#metrics-monitoring-and-logging)
  - [Miscellaneous](#miscellaneous)
  - [Templates](#templates)
- [Example Bots](#example-bots)
  - [Reference implementations](#reference-implementations)
  - [Community and moderation](#community-and-moderation)
  - [Frameworks](#frameworks)
  - [Music and games](#music-and-games)
  - [Specialized](#specialized)
  - [Multipurpose](#multipurpose)
- [Blog Posts, Guides and Tutorials](#blog-posts-guides-and-tutorials)
- [Community Gists and Snippets](#community-gists-and-snippets)
  - [Help Commands](#help-commands)
  - [Error Handling](#error-handling)
  - [Components and UI](#components-and-ui)
  - [Components V2](#components-v2)
  - [Cogs and Commands](#cogs-and-commands)
  - [Other Snippets](#other-snippets)
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
- [Official Examples](https://github.com/Rapptz/discord.py/tree/master/examples) - Example bots and snippets from the upstream repo. <span title="Last activity 2026-09">⚡</span>
- [Discord.py GitHub](https://github.com/Rapptz/discord.py) - Upstream source repository. <span title="Last activity 2026-09">⚡</span>

## Libraries and Extensions

### Utilities

- [Kyrela/discore](https://github.com/Kyrela/discore) - Bot bootstrap with log and error tracking. <span title="Last activity 2026-10">⚡</span>
- [tibue99/ezcord](https://github.com/tibue99/ezcord) - Cogs, i18n, error webhooks, and embed helpers; also works with Pycord. <span title="Last activity 2026-10">⚡</span>
- [Soheab/discord-ext-subcommands](https://github.com/Soheab/discord-ext-subcommands) - Define prefix, slash, and hybrid subcommands across files and cogs. <span title="Last activity 2026-09">⚡</span>
- [python-discord/bot-core](https://github.com/python-discord/bot-core) - Shared utilities used by Python Discord's bots. <span title="Last activity 2026-09">⚡</span>
- [clari7744/DPyUtils](https://github.com/clari7744/DPyUtils) - Duration parsing, extra converters, and a context editor that re-runs commands when the user edits their message. <span title="Last activity 2026-04">🕰️</span>
- [mikeshardmind/discord-scheduler](https://github.com/mikeshardmind/discord-scheduler) - Persistent SQLite-backed task scheduler with timezone-aware wall times. <span title="Last activity 2025-02">🕰️</span>
- [Soheab/discord-ext-custom_interaction](https://github.com/Soheab/discord-ext-custom_interaction) - Subclass `discord.Interaction` with helpers such as `send` and `author`. <span title="Last activity 2025-01">🕰️</span>
- [InterStella0/starlight-dpy](https://github.com/InterStella0/starlight-dpy) - Paginated help commands, inline views, and converters. Pre-alpha; not for production. <span title="Last activity 2024-02">💤</span>
- [Voxel-Fox-Ltd/VoxelBotUtils](https://github.com/Voxel-Fox-Ltd/VoxelBotUtils) - Config, database, logging, error handling, and help-command helpers, built for Novus. <span title="Last activity 2024-01">💤</span>
- [Soheab/discord.py-listen-overloads](https://github.com/Soheab/discord.py-listen-overloads) - Type stubs that add overloads to `@commands.Bot.listen` for library events. <span title="Last activity 2023-12">💤</span>
- [timelessnesses/dpyhr](https://github.com/timelessnesses/dpyhr) - Reloads cogs on save using the built-in cog loader. <span title="Last activity 2023-04">💤</span>
- [tanrbobanr/dpy-check](https://github.com/tanrbobanr/dpy-check) - Composable, dynamic checks for prefix and application commands. <span title="Last activity 2023-01">💤</span>

### Testing and Debugging

- [python-discord/snekbox](https://github.com/python-discord/snekbox) - NSJail sandbox for evaluating untrusted Python, used by Python Discord. <span title="Last activity 2026-10">⚡</span>
- [CraftSpider/dpytest](https://github.com/CraftSpider/dpytest) - Fake Discord backend for writing bot tests. <span title="Last activity 2026-06">⚡</span>
- [scarletcafe/jishaku](https://github.com/scarletcafe/jishaku) - REPL, extension reload, and debug cog for running bots. <span title="Last activity 2026-04">🕰️</span>

### UI

- [thegamecracks/discord-ext-pager](https://github.com/thegamecracks/discord-ext-pager) - Paginator with an API close to discord-ext-menus. <span title="Last activity 2026-10">⚡</span>
- [keizaiya/discord-ext-flow](https://github.com/keizaiya/discord-ext-flow) - State-machine control flow on top of `discord.ui`. <span title="Last activity 2026-10">⚡</span>
- [HollowTheSilver/CascadeUI](https://github.com/HollowTheSilver/CascadeUI) - Redux-style centralized state, persistence, and Components V2 patterns. <span title="Last activity 2026-10">⚡</span>
- [Defxult/reactionmenu](https://github.com/Defxult/reactionmenu) - Paginator with buttons, reactions, and select-based categories. <span title="Last activity 2026-05">⚡</span>
- [Soheab/discord-py-paginators](https://github.com/Soheab/discord-py-paginators) - Button and other paginator types with published docs. <span title="Last activity 2025-10">🕰️</span>
- [Soheab/cv2examples](https://github.com/Soheab/cv2examples) - Screenshots and sample layouts for Components V2. <span title="Last activity 2025-07">🕰️</span>
- [Soheab/modal-paginator](https://github.com/Soheab/modal-paginator) - Paginate a Modal across pages using buttons. <span title="Last activity 2025-05">🕰️</span>
- [philskillz-coder/discord-py-paginator](https://github.com/philskillz-coder/discord-py-paginator) - View-based embed paginator. <span title="Last activity 2025-04">🕰️</span>
- [Soheab/discord-ext-embeds](https://github.com/Soheab/discord-ext-embeds) - Embed constructor with author/footer shortcuts, file media, and character-limit checks. <span title="Last activity 2025-03">🕰️</span>
- [OnceYT/dpy-paginator](https://github.com/OnceYT/dpy-paginator) - Dependency-free embed paginator. <span title="Last activity 2024-10">💤</span>
- [sizumita/discord-ext-ui](https://github.com/sizumita/discord-ext-ui) - Declarative SwiftUI-style views with reactive state; works with Pycord too. <span title="Last activity 2024-10">💤</span>
- [Modern-Realm/discord_btns_menus](https://github.com/Modern-Realm/discord_btns_menus) - Buttons, select menus, combinations, and pagination; also supports related forks. <span title="Last activity 2024-06">💤</span>
- [LiBa001/disputils](https://github.com/LiBa001/disputils) - Pagination, confirmation dialogs, and small UI helpers. <span title="Last activity 2024-05">💤</span>
- [vcv88/discord-ext-dyn](https://github.com/vcv88/discord-ext-dyn) - Dynamic creation of modals, buttons, and select menus. <span title="Last activity 2024-01">💤</span>
- [Seniatical/dpy-paginator](https://github.com/Seniatical/dpy-paginator) - Button and dropdown pagination. <span title="Last activity 2023-04">💤</span>

### Inter-Process Communication

- [No767/discord-ext-ipcx](https://github.com/No767/discord-ext-ipcx) - Maintained IPC extension for splitting the bot across processes. <span title="Last activity 2026-10">⚡</span>

### Voice receive

- [discord-ext-voice-recv](https://github.com/imayhaveborkedit/discord-ext-voice-recv) - Receive and process users' voice packets. <span title="Last activity 2025-06">🕰️</span>
- [Sheppsu/discord-ext-listening](https://github.com/Sheppsu/discord-ext-listening) - Voice receive via multiprocessing. <span title="Last activity 2024-02">💤</span>

### Voice send

- [tuna2134/discord-ext-songbird](https://github.com/tuna2134/discord-ext-songbird) - Rust Songbird voice client wrapper; Linux and macOS only. <span title="Last activity 2026-10">⚡</span>

### Lavalink

- [devoxin/Lavalink.py](https://github.com/devoxin/Lavalink.py) - Lavalink client with multi-node load balancing, filters, and custom sources. <span title="Last activity 2026-10">⚡</span>
- [cloudwithax/pomice](https://github.com/cloudwithax/pomice) - Lavalink client with Spotify and Apple Music querying. <span title="Last activity 2026-10">⚡</span>
- [ooliver1/mafic](https://github.com/ooliver1/mafic) - Typed Lavalink client that also supports nextcord, disnake, and Pycord. <span title="Last activity 2026-10">⚡</span>
- [PyLav/PyLav](https://github.com/PyLav/PyLav) - Lavalink wrapper aimed at bots including Red-DiscordBot. <span title="Last activity 2026-10">⚡</span>
- [sonolink/sonolink](https://github.com/sonolink/sonolink) - Typed Lavalink v4 client built on msgspec; also supports Pycord and disnake. <span title="Last activity 2026-10">⚡</span>
- [ParrotXray/lava-lyra](https://github.com/ParrotXray/lava-lyra) - Lavalink v4 and Nodelink v3 client that also supports Pycord. <span title="Last activity 2026-08">⚡</span>
- [PythonistaGuild/Wavelink](https://github.com/PythonistaGuild/Wavelink) - Async Lavalink v4 client. <span title="Last activity 2026-07">⚡</span>
- [HazemMeqdad/lavaplay.py](https://github.com/HazemMeqdad/lavaplay.py) - Lavalink v4 node manager that works with any async Discord wrapper. <span title="Last activity 2026-05">⚡</span>
- [Cog-Creators/Red-Lavalink](https://github.com/Cog-Creators/Red-Lavalink) - Lavalink client used by Red-DiscordBot, usable in any bot. <span title="Last activity 2026-03">🕰️</span>

### Authentication

- [Soheab/oauthcord.py](https://github.com/Soheab/oauthcord.py) - Async OAuth2 client with typed REST models; not a bot framework. <span title="Last activity 2026-10">⚡</span>
- [Rapptz/open-collective-discord-auth](https://github.com/Rapptz/open-collective-discord-auth) - Linked-role auth server for Open Collective membership. <span title="Last activity 2026-06">⚡</span>
- [treeben77/discord-oauth2.py](https://github.com/treeben77/discord-oauth2.py) - OAuth2 and Linked Roles REST wrapper. <span title="Last activity 2026-01">🕰️</span>

### Metrics, Monitoring, and Logging

- [EthanC/Loguru-Discord](https://github.com/EthanC/Loguru-Discord) - Loguru sink that posts logs to a webhook. <span title="Last activity 2026-10">⚡</span>
- [discord-ext-prometheus](https://github.com/ApolloRoboto/discord.py-ext-prometheus) - Prometheus metrics exporter for running bots. <span title="Last activity 2025-02">🕰️</span>
- [python-discord/metricity](https://github.com/python-discord/metricity) - Metric collection used on the Python Discord server. <span title="Last activity 2024-09">💤</span>

### Miscellaneous

- [Skelmis/Discord-Anti-Spam](https://github.com/Skelmis/Discord-Anti-Spam) - Automatic spam handling for commands and messages. <span title="Last activity 2026-07">⚡</span>
- [mahtoid/DiscordChatExporterPy](https://github.com/mahtoid/DiscordChatExporterPy) - Export channel history to HTML transcripts. <span title="Last activity 2026-05">⚡</span>
- [Tom-the-Bomb/Discord-Games](https://github.com/Tom-the-Bomb/Discord-Games) - Drop-in games such as chess, Connect Four, hangman, and 2048, played through reactions or buttons. <span title="Last activity 2026-03">🕰️</span>
- [YousefEZ/discord-qalib](https://github.com/YousefEZ/discord-qalib) - XML templates for embeds and paginated menus. <span title="Last activity 2026-01">🕰️</span>
- [Bluenix2/discord-typings](https://github.com/Bluenix2/discord-typings) - TypedDicts for Discord gateway and HTTP payloads. <span title="Last activity 2025-04">🕰️</span>
- [CasuallyCalm/discord-pretty-help](https://github.com/CasuallyCalm/discord-pretty-help) - Embed-based replacement for the built-in help command. <span title="Last activity 2023-07">💤</span>

### Templates

- [kkrypt0nn/Python-Discord-Bot-Template](https://github.com/kkrypt0nn/Python-Discord-Bot-Template) - Starter project for a personalized bot. <span title="Last activity 2026-10">⚡</span>
- [PaulMarisOUMary/Discord-Bot](https://github.com/PaulMarisOUMary/Discord-Bot) - 2.x starter with hybrid commands, Docker, logging, and a database. <span title="Last activity 2026-10">⚡</span>

## Example Bots

### Reference implementations

- [AlexFlipnote/discord_bot.py](https://github.com/AlexFlipnote/discord_bot.py) - Minimal starter bot. <span title="Last activity 2026-10">⚡</span>
- [avizum/alpine](https://github.com/avizum/alpine) - Public source for a general-purpose bot; author recommends the hosted instance. <span title="Last activity 2026-10">⚡</span>
- [AbstractUmbra/Mipha](https://github.com/AbstractUmbra/Mipha) - Umbra's personal bot, forked from RoboDanny and kept on latest library releases. <span title="Last activity 2026-10">⚡</span>
- [Kile/Killua](https://github.com/Kile/Killua) - Games, moderation, and todo lists, plus extra algorithm notes in-tree. <span title="Last activity 2026-08">⚡</span>
- [Rapptz/RoboDanny](https://github.com/Rapptz/RoboDanny) - Rapptz's production bot; commonly used as a reference implementation. <span title="Last activity 2026-06">⚡</span>
- [onerandomusername/monty-python](https://github.com/onerandomusername/monty-python) - Helper bot for Python project development. <span title="Last activity 2026-02">🕰️</span>

### Community and moderation

- [python-discord/bot](https://github.com/python-discord/bot) - Moderation, utils, and community tools for Python Discord. <span title="Last activity 2026-10">⚡</span>
- [modmail-dev/Modmail](https://github.com/modmail-dev/Modmail) - Shared staff inbox, similar to Reddit Modmail. <span title="Last activity 2026-10">⚡</span>
- [python-discord/sir-lancebot](https://github.com/python-discord/sir-lancebot) - On-ramp bot for new open-source contributors at Python Discord. <span title="Last activity 2026-09">⚡</span>
- [Tortoise-Community/tortoise-bot](https://github.com/Tortoise-Community/tortoise-bot) - Community bot for the Tortoise Discord. <span title="Last activity 2026-09">⚡</span>
- [python-discord/sir-robin](https://github.com/python-discord/sir-robin) - Event-management bot for Python Discord. <span title="Last activity 2026-08">⚡</span>
- [fourjr/rainbot](https://github.com/fourjr/rainbot) - Moderation bot with automod and logging. <span title="Last activity 2026-04">🕰️</span>
- [PythonistaGuild/Pythonista-Bot](https://github.com/PythonistaGuild/Pythonista-Bot) - Guild bot for the Pythonista Guild server. <span title="Last activity 2025-02">🕰️</span>
- [DeJayDev/speedboat](https://github.com/DeJayDev/speedboat) - Tools for running large community servers. <span title="Last activity 2024-09">💤</span>

### Frameworks

- [Cog-Creators/Red-DiscordBot](https://github.com/Cog-Creators/Red-DiscordBot) - Self-hosted modular bot with a large cog ecosystem. <span title="Last activity 2026-10">⚡</span>

### Music and games

- [ChocoMeow/Vocard](https://github.com/ChocoMeow/Vocard) - Music bot for YouTube, SoundCloud, Spotify, and Twitch. <span title="Last activity 2026-10">⚡</span>
- [Ballsdex-Team/BallsDex-DiscordBot](https://github.com/Ballsdex-Team/BallsDex-DiscordBot) - Collect and trade countryballs. <span title="Last activity 2026-10">⚡</span>
- [seriaati/hoyo-buddy](https://github.com/seriaati/hoyo-buddy) - User-installable bot for Genshin Impact, Honkai: Star Rail, and other Hoyoverse games. <span title="Last activity 2026-10">⚡</span>
- [poketwo/poketwo](https://github.com/poketwo/poketwo) - Pokémon catching and collecting, in the Pokécord style. <span title="Last activity 2025-02">🕰️</span>

### Specialized

- [statch/gitbot](https://github.com/statch/gitbot) - GitHub notifications and developer tools. <span title="Last activity 2026-10">⚡</span>
- [Hunter87ff/Spruce](https://github.com/Hunter87ff/Spruce) - Tournament and server management. <span title="Last activity 2026-10">⚡</span>
- [Yuuzi261/Tweetcord](https://github.com/Yuuzi261/Tweetcord) - Posts new tweets from followed X/Twitter accounts to chosen channels. <span title="Last activity 2026-10">⚡</span>
- [mikeywhiston/ERM](https://github.com/mikeywhiston/ERM) - Staff tools aimed at Roblox communities. <span title="Last activity 2026-09">⚡</span>
- [jakobdylanc/llmcord](https://github.com/jakobdylanc/llmcord) - LLM frontend for OpenAI-compatible APIs. <span title="Last activity 2026-08">⚡</span>
- [cheran-senthil/TLE](https://github.com/cheran-senthil/TLE) - Competitive programming helper for Codeforces and similar sites. <span title="Last activity 2026-03">🕰️</span>

### Multipurpose

- [joinemm/miso-bot](https://github.com/joinemm/miso-bot) - General-purpose bot with Last.fm and K-pop commands. <span title="Last activity 2026-10">⚡</span>
- [Axobot-org/Axobot](https://github.com/Axobot-org/Axobot) - Multilingual general-purpose bot with moderation, XP, and Minecraft lookups. <span title="Last activity 2026-10">⚡</span>
- [Iapetus-11/Villager-Bot](https://github.com/Iapetus-11/Villager-Bot) - Minecraft-themed bot with server status checks, pixel art, and an economy game; sharded across clusters. <span title="Last activity 2026-10">⚡</span>
- [wasi-master/wm_bot](https://github.com/wasi-master/wm_bot) - General-purpose bot with a large command set. <span title="Last activity 2026-07">⚡</span>
- [DTS-11/PizzaHat](https://github.com/DTS-11/PizzaHat) - General-purpose bot with a public website and AGPL source. <span title="Last activity 2026-05">⚡</span>
- [Nirlep5252/EpicBot](https://github.com/Nirlep5252/EpicBot) - General-purpose bot with a large public command set. <span title="Last activity 2025-07">🕰️</span>

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

- [voidoak/Implementing Help](https://gist.github.com/voidoak/4f34922888eeca04e1bba8c0ebd2f948) - Tutorial on implementing your own help command. <span title="Last activity 2026-03">🕰️</span>
- [InterStella0/HelpCommand walkthrough](https://gist.github.com/InterStella0/b78488fb28cadf279dfd3164b9f0cf96) - Walkthrough for subclassing HelpCommand. <span title="Last activity 2025-12">🕰️</span>
- [nonchris/Custom Help Command](https://gist.github.com/nonchris/1c7060a14a9d94e7929aa2ef14c41bc2) - Advanced custom help command example. <span title="Last activity 2024-08">💤</span>
- [Rapptz/Embed Help Command](https://gist.github.com/Rapptz/31a346ed1eb545ddeb0d451d81a60b3b) - Embed-based help command example from the library author. <span title="Last activity 2024-07">💤</span>
- [Gobot1234/Sub-classing Help](https://gist.github.com/Gobot1234/45cad24df63fc144e85a7f8c85812567) - Guide to subclassing the help command. <span title="Last activity 2021-07">💤</span>

### Error Handling

- [EvieePy/Error Handling](https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612) - Error handling for prefix and app commands. <span title="Last activity 2026-10">⚡</span>
- [irregularunit/Command Error Handler](https://gist.github.com/irregularunit/0221164777a476c653e36b49439b7b06) - Structured command error handler example. <span title="Last activity 2023-07">💤</span>
- [Jeftaei/AppCommandErrorhandler.py](https://gist.github.com/Jeftaei/d0bad5044f1192a4c454f95a6b591d53) - Error handler covering prefix and app commands. <span title="Last activity 2023-05">💤</span>

### Components and UI

- [Soheab/Simple Button Paginator](https://gist.github.com/Soheab/f226fc06a3468af01ea3168c95b30af8) - Small paginator with three buttons. <span title="Last activity 2026-04">🕰️</span>
- [Soheab/Global View](https://gist.github.com/Soheab/cfd769870b7b6eaf00a7aebf5293a622) - Pattern for a globally registered view. <span title="Last activity 2026-04">🕰️</span>
- [lykn/Buttons](https://gist.github.com/lykn/bac99b06d45ff8eed34c2220d86b6bf4) - How to make buttons in v2. <span title="Last activity 2026-02">🕰️</span>
- [lykn/Selects or Dropdowns](https://gist.github.com/lykn/a2b68cb790d6dad8ecff75b2aa450f23) - Select menus in v2. <span title="Last activity 2026-01">🕰️</span>
- [InterStella0/Pagination Walkthrough](https://gist.github.com/InterStella0/454cc51e05e60e63b81ea2e8490ef140) - Walkthrough of action-based pagination. <span title="Last activity 2025-04">🕰️</span>
- [imptype/Message Maker](https://gist.github.com/imptype/7b35c6769684fb68178e5719e5f81b6d) - Embed/message builder command. <span title="Last activity 2025-03">🕰️</span>
- [esmaycat/Message Components](https://gist.github.com/esmaycat/500eafdad0aaf278b94c612764688976) - Using message components in 2.0. <span title="Last activity 2025-02">🕰️</span>
- [Soheab/wait_for Modal](https://gist.github.com/Soheab/f46fee27498aad4a8962d59b6f0415c6) - Wait for user input with a modal. <span title="Last activity 2024-11">🕰️</span>
- [mikeshardmind/List Menu](https://gist.github.com/mikeshardmind/bff6f937032455d83b8f1724ef73575a) - List menu pagination snippet. <span title="Last activity 2024-03">💤</span>
- [quackbarc/2.0 Paginators](https://gist.github.com/quackbarc/31e5cd789d232ad0d263511bb1a506e8) - Paginator examples for 2.0. <span title="Last activity 2022-03">💤</span>

### Components V2

- [Soheab/Components V2 to LayoutView](https://gist.github.com/Soheab/ab7a833725f95a84a8f7fa17995cb36c) - Mapping Components V2 to LayoutView. <span title="Last activity 2026-07">⚡</span>
- [Soheab/CV2 Paginator](https://gist.github.com/Soheab/891c39d7294b1bdbadc7ecf35ce51cc5) - Components V2 paginator. <span title="Last activity 2026-04">🕰️</span>
- [Soheab/Embed to Container](https://gist.github.com/Soheab/cf356c62a6134508869bf40640b04856) - Convert an embed into a Components V2 container. <span title="Last activity 2025-11">🕰️</span>

### Cogs and Commands

- [Soheab/self.bot in Cogs](https://gist.github.com/Soheab/cf387b753da32eb02f3228c2e32bb03f) - How `self.bot` works inside a cog. <span title="Last activity 2026-08">⚡</span>
- [EvieePy/Cogs Example](https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be) - Classic cogs and extension layout. <span title="Last activity 2025-08">🕰️</span>
- [Soheab/wait_for in Commands](https://gist.github.com/Soheab/e73ab6f66881ee4102be37815da3a24e) - Examples of `wait_for` inside ext.commands. <span title="Last activity 2025-06">🕰️</span>
- [LeoCx1000/MentionableTree implementation](https://gist.github.com/LeoCx1000/021dc52981299b95ea7790416e4f5ca4) - Mentionable CommandTree so slash commands can be mentioned. <span title="Last activity 2025-05">🕰️</span>
- [Painezor/Checks](https://gist.github.com/Painezor/eb2519022cd2c907b56624105f94b190) - Built-in checks for the commands extension. <span title="Last activity 2025-04">🕰️</span>
- [Samarthh2601/App Commands Walkthrough](https://gist.github.com/Samarthh2601/b6f57065f394b54f43666037ade38d32) - Walkthrough for application commands. <span title="Last activity 2025-01">🕰️</span>
- [Soheab/Any-Permission Check](https://gist.github.com/Soheab/ec3f40f9f54add0dba787783719331f8) - Custom check that passes if the user has any of the given permissions. <span title="Last activity 2024-07">💤</span>
- [Ikusaba-san/Cog Methods](https://gist.github.com/Ikusaba-san/69115b79d33e05ed07ec4a4f14db83b1) - List of special cog methods. <span title="Last activity 2021-05">💤</span>

### Other Snippets

- [kkrypt0nn/ANSI Colors on Discord](https://gist.github.com/kkrypt0nn/a02506f3712ff2d1c8ca7c9e0aed7c06) - ANSI color codes in Discord code blocks. <span title="Last activity 2026-10">⚡</span>
- [LeviSnoot/Discord Timestamps](https://gist.github.com/LeviSnoot/d9147767abeef2f770e9ddcd91eb85aa) - Discord timestamp markdown syntax. <span title="Last activity 2026-10">⚡</span>
- [advaith1/Intents Explainer](https://gist.github.com/advaith1/e69bcc1cdd6d0087322734451f15aa2f) - Gateway and privileged intents: statuses, members, and message content. <span title="Last activity 2026-09">⚡</span>
- [mikeshardmind/SQLite Examples](https://gist.github.com/mikeshardmind/d7d2c6cb19b53ab76b7d401b2716df5d) - Common SQLite patterns for bots. <span title="Last activity 2026-09">⚡</span>
- [Soheab/APIs for Discord Bots](https://gist.github.com/Soheab/332ba85f8989648449c71bdc8ef32368) - Community list of APIs commonly used with Discord bots. <span title="Last activity 2026-08">⚡</span>
- [Soheab/Threads](https://gist.github.com/Soheab/4709e335474784d8a1877812f6d0c354) - Creating and managing Discord threads. <span title="Last activity 2026-07">⚡</span>
- [4Kaylum/Discord.py Tutorial](https://gist.github.com/4Kaylum/a1e9f31c31b17386c36f017d3c59cdcc) - Simple bot tutorial. <span title="Last activity 2026-05">⚡</span>
- [AkshuAgarwal/Interactions](https://gist.github.com/AkshuAgarwal/bc7d45bcecd5d29de4d6d7904e8b8bd8) - Intro to interactions and how to handle them. <span title="Last activity 2026-02">🕰️</span>
- [Soheab/Voice Channel Status](https://gist.github.com/Soheab/e9a747f5c8fae43447a5611e483b4beb) - React when a voice channel status is set or changed. <span title="Last activity 2026-02">🕰️</span>
- [Soheab/discord.Colour](https://gist.github.com/Soheab/d9cf3f40e34037cfa544f464fc7d919e) - Reference for discord.Colour helpers. <span title="Last activity 2026-02">🕰️</span>
- [scragly/Learning discord.py](https://gist.github.com/scragly/095b5278a354d46e86f02d643fc3d64b) - Setup, core concepts, and a resource list for learning the library. <span title="Last activity 2025-12">🕰️</span>
- [Soheab/No Message Content Intent Ideas](https://gist.github.com/Soheab/a6229dbbe3acf3ce9a4625bf9e7177da) - Command ideas that work without the privileged message content intent. <span title="Last activity 2025-12">🕰️</span>
- [cibere/Defer Response](https://gist.github.com/cibere/7e1356575780e716d2e3a23ea2bcf6da) - Acknowledge an interaction and respond later, up to 15 minutes. <span title="Last activity 2025-02">🕰️</span>
- [Soheab/Server Tag](https://gist.github.com/Soheab/d5e7fdbca3db94629cf87f1178096aab) - Overflow copy of a long official-server tag that exceeded Discord's character limit. <span title="Last activity 2024-10">💤</span>
- [philskillz-coder/Color Transformer](https://gist.github.com/philskillz-coder/c6bee6c8e258ad56afb01840df26a1fa) - Color transformer and autocomplete. <span title="Last activity 2023-06">💤</span>
- [CuteFwan/wait_for Multiple Events](https://gist.github.com/CuteFwan/ded1bf520d71baac18726fa2e0554f0f) - Waiting for more than one Discord event at a time. <span title="Last activity 2021-08">💤</span>

## Additional Resources

- [Permissions Calculator](https://discordapi.com/permissions.html) - Build bot invite links with a chosen permission bitfield.
- [Discord Community Resources](https://discord.com/developers/docs/topics/community-resources) - Official index of libraries, calculators, and embed tools.
- [Intent Calculator](https://ziad87.net/intents/) - Build a gateway intents bitfield for Identify.
- [Embed Visualizer](https://leovoel.github.io/embed-visualizer/) - Live embed designer with generated library snippets.
- [scarletcafe/discord.py-docker](https://github.com/scarletcafe/discord.py-docker) - Source for the `gorialis/discord.py` Docker images with the library preinstalled. <span title="Last activity 2026-04">🕰️</span>
- [Soheab/discord.py-tags](https://github.com/Soheab/discord.py-tags) - Overflow copies of long tags from the official library Discord. <span title="Last activity 2024-12">🕰️</span>
- [Soheab/dpy-badhosts](https://github.com/Soheab/dpy-badhosts) - Hosts the community generally warns against using for bots. <span title="Last activity 2024-11">🕰️</span>
- [Soheab/dpy-missing-features](https://github.com/Soheab/dpy-missing-features) - Discord API features the library does not yet expose. <span title="Last activity 2024-08">💤</span>
- [Rapptz/asqlite](https://github.com/Rapptz/asqlite) - Async wrapper around sqlite3. <span title="Last activity 2024-07">💤</span>
- [discord-interactions-python](https://github.com/discord/discord-interactions-python) - Official helpers for verifying HTTP interaction signatures. <span title="Last activity 2024-04">💤</span>

## Forks and Wrappers

disnake, nextcord, Novus, pycord, and discord.py-message-components are discord.py forks. hikari, hata, interactions.py, and discord.http are independent wrappers, not drop-in replacements for discord.py.

- [disnake](https://github.com/DisnakeDev/disnake) - Async Discord API wrapper, forked from discord.py. <span title="Last activity 2026-10">⚡</span>
- [nextcord](https://github.com/nextcord/nextcord) - API wrapper forked from discord.py. <span title="Last activity 2026-10">⚡</span>
- [pycord](https://github.com/Pycord-Development/pycord) - Maintained fork of discord.py. <span title="Last activity 2026-10">⚡</span>
- [hikari](https://github.com/hikari-py/hikari) - Independent async wrapper, not a drop-in replacement. <span title="Last activity 2026-10">⚡</span>
- [interactions.py](https://github.com/interactions-py/interactions.py) - Independent bot framework, not a drop-in replacement. <span title="Last activity 2026-10">⚡</span>
- [hata](https://github.com/HuyaneMatsu/hata) - Independent async wrapper, not a drop-in replacement. <span title="Last activity 2026-10">⚡</span>
- [AlexFlipnote/discord.http](https://github.com/AlexFlipnote/discord.http) - HTTP-interactions-first library with optional gateway and cache control. <span title="Last activity 2026-10">⚡</span>
- [Novus](https://github.com/Voxel-Fox-Ltd/Novus) - Async API wrapper forked from discord.py, used by VoxelBotUtils. <span title="Last activity 2026-07">⚡</span>
- [mccoderpy/discord.py-message-components](https://github.com/mccoderpy/discord.py-message-components) - Fork that added message components before they landed upstream. <span title="Last activity 2025-06">🕰️</span>

## Related

- [Discord Library Comparison](https://libs.advaith.io) - Feature matrix across Discord libraries.
- [jacc/awesome-discord](https://github.com/jacc/awesome-discord) - Clients, bots, libraries, and related tools. <span title="Last activity 2026-05">⚡</span>
- [awesome-discord-communities](https://github.com/mhxion/awesome-discord-communities) - Programmer Discord communities. <span title="Last activity 2026-04">🕰️</span><!-- END CONTENT -->

## Contributing

[Contributions of any kind welcome, just follow the guidelines](contributing.md)!

### Contributors

[Thanks goes to these contributors](https://github.com/kzndotsh/awesome-discordpy/graphs/contributors)!
