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
- [Official Examples](https://github.com/Rapptz/discord.py/tree/master/examples) - Example bots and snippets from the upstream repo (last activity 2026-07).
- [Discord.py GitHub](https://github.com/Rapptz/discord.py) - Upstream source repository (last activity 2026-07).
- [Discord.py Discord Server](https://discord.gg/dpy) - Official community Discord.

## Libraries and Extensions

### Utilities

- [InterStella0/starlight-dpy](https://github.com/InterStella0/starlight-dpy) - Paginated help commands, inline views, and converters. Pre-alpha; not for production (last activity 2024-02).
- [clari7744/DPyUtils](https://github.com/clari7744/DPyUtils) - Duration parsing, extra converters, and a context editor that re-runs commands when the user edits their message (last activity 2026-04).
- [tanrbobanr/dpy-check](https://github.com/tanrbobanr/dpy-check) - Composable, dynamic checks for prefix and application commands (last activity 2023-01).
- [cogwatch](https://pypi.org/project/cogwatch/) - Hot-reload command files as you edit them.
- [timelessnesses/dpyhr](https://github.com/timelessnesses/dpyhr) - Reloads cogs on save using the built-in cog loader (last activity 2023-04).
- [mikeshardmind/discord-scheduler](https://github.com/mikeshardmind/discord-scheduler) - Persistent SQLite-backed task scheduler with timezone-aware wall times (last activity 2025-02).
- [Voxel-Fox-Ltd/VoxelBotUtils](https://github.com/Voxel-Fox-Ltd/VoxelBotUtils) - Config, database, logging, error handling, and help-command helpers, built for Novus (last activity 2024-01).
- [Kyrela/discore](https://github.com/Kyrela/discore) - Bot bootstrap with log and error tracking (last activity 2026-01).
- [Soheab/discord.py-listen-overloads](https://github.com/Soheab/discord.py-listen-overloads) - Type stubs that add overloads to `@commands.Bot.listen` for library events (last activity 2023-12).
- [Soheab/discord-ext-subcommands](https://github.com/Soheab/discord-ext-subcommands) - Define prefix, slash, and hybrid subcommands across files and cogs (last activity 2026-03).
- [Soheab/discord-ext-custom_interaction](https://github.com/Soheab/discord-ext-custom_interaction) - Subclass `discord.Interaction` with helpers such as `send` and `author` (last activity 2025-01).
- [tibue99/ezcord](https://github.com/tibue99/ezcord) - Cogs, i18n, error webhooks, and embed helpers; also works with Pycord (last activity 2026-07).
- [python-discord/bot-core](https://github.com/python-discord/bot-core) - Shared utilities used by Python Discord's bots (last activity 2026-05).

### Testing and Debugging

- [scarletcafe/jishaku](https://github.com/scarletcafe/jishaku) - REPL, extension reload, and debug cog for running bots (last activity 2026-04).
- [CraftSpider/dpytest](https://github.com/CraftSpider/dpytest) - Fake Discord backend for writing bot tests (last activity 2026-06).
- [python-discord/snekbox](https://github.com/python-discord/snekbox) - NSJail sandbox for evaluating untrusted Python, used by Python Discord (last activity 2026-08).

### UI

- [Defxult/reactionmenu](https://github.com/Defxult/reactionmenu) - Paginator with buttons, reactions, and select-based categories (last activity 2026-05).
- [Soheab/discord-py-paginators](https://github.com/Soheab/discord-py-paginators) - Button and other paginator types with published docs (last activity 2025-10).
- [Soheab/modal-paginator](https://github.com/Soheab/modal-paginator) - Paginate a Modal across pages using buttons (last activity 2025-05).
- [philskillz-coder/discord-py-paginator](https://github.com/philskillz-coder/discord-py-paginator) - View-based embed paginator (last activity 2025-04).
- [thegamecracks/discord-ext-pager](https://github.com/thegamecracks/discord-ext-pager) - Paginator with an API close to discord-ext-menus (last activity 2026-08).
- [OnceYT/dpy-paginator](https://github.com/OnceYT/dpy-paginator) - Dependency-free embed paginator (last activity 2024-10).
- [Soheab/discord-ext-embeds](https://github.com/Soheab/discord-ext-embeds) - Embed constructor with author/footer shortcuts, file media, and character-limit checks (last activity 2025-03).
- [keizaiya/discord-ext-flow](https://github.com/keizaiya/discord-ext-flow) - State-machine control flow on top of `discord.ui` (last activity 2026-08).
- [sizumita/discord-ext-ui](https://github.com/sizumita/discord-ext-ui) - Declarative SwiftUI-style views with reactive state; works with Pycord too (last activity 2024-10).
- [Seniatical/dpy-paginator](https://github.com/Seniatical/dpy-paginator) - Button and dropdown pagination (last activity 2023-04).
- [vcv88/discord-ext-dyn](https://github.com/vcv88/discord-ext-dyn) - Dynamic creation of modals, buttons, and select menus (last activity 2024-01).
- [Modern-Realm/discord_btns_menus](https://github.com/Modern-Realm/discord_btns_menus) - Buttons, select menus, combinations, and pagination; also supports related forks (last activity 2024-06).
- [HollowTheSilver/CascadeUI](https://github.com/HollowTheSilver/CascadeUI) - Redux-style centralized state, persistence, and Components V2 patterns (last activity 2026-08).
- [LiBa001/disputils](https://github.com/LiBa001/disputils) - Pagination, confirmation dialogs, and small UI helpers (last activity 2024-05).
- [Soheab/cv2examples](https://github.com/Soheab/cv2examples) - Screenshots and sample layouts for Components V2 (last activity 2025-07).

### Inter-Process Communication

- [No767/discord-ext-ipcx](https://github.com/No767/discord-ext-ipcx) - Maintained IPC extension for splitting the bot across processes (last activity 2026-08).

### Voice receive

- [discord-ext-voice-recv](https://github.com/imayhaveborkedit/discord-ext-voice-recv) - Receive and process users' voice packets (last activity 2025-06).
- [Sheppsu/discord-ext-listening](https://github.com/Sheppsu/discord-ext-listening) - Voice receive via multiprocessing (last activity 2024-02).

### Voice send

- [tuna2134/discord-ext-songbird](https://github.com/tuna2134/discord-ext-songbird) - Rust Songbird voice client wrapper; Linux and macOS only (last activity 2026-07).

### Lavalink

- [PythonistaGuild/Wavelink](https://github.com/PythonistaGuild/Wavelink) - Async Lavalink v4 client (last activity 2026-07).
- [devoxin/Lavalink.py](https://github.com/devoxin/Lavalink.py) - Lavalink client with multi-node load balancing, filters, and custom sources (last activity 2026-06).
- [cloudwithax/pomice](https://github.com/cloudwithax/pomice) - Lavalink client with Spotify and Apple Music querying (last activity 2026-07).
- [ooliver1/mafic](https://github.com/ooliver1/mafic) - Typed Lavalink client that also supports nextcord, disnake, and Pycord (last activity 2026-08).
- [PyLav/PyLav](https://github.com/PyLav/PyLav) - Lavalink wrapper aimed at bots including Red-DiscordBot (last activity 2026-08).
- [ParrotXray/lava-lyra](https://github.com/ParrotXray/lava-lyra) - Lavalink v4 and Nodelink v3 client that also supports Pycord (last activity 2026-08).

### Authentication

- [treeben77/discord-oauth2.py](https://github.com/treeben77/discord-oauth2.py) - OAuth2 and Linked Roles REST wrapper (last activity 2026-01).
- [Soheab/oauthcord.py](https://github.com/Soheab/oauthcord.py) - Async OAuth2 client with typed REST models; not a bot framework (last activity 2026-08).
- [Rapptz/open-collective-discord-auth](https://github.com/Rapptz/open-collective-discord-auth) - Linked-role auth server for Open Collective membership (last activity 2026-06).

### Metrics, Monitoring, and Logging

- [discord-ext-prometheus](https://github.com/ApolloRoboto/discord.py-ext-prometheus) - Prometheus metrics exporter for running bots (last activity 2025-02).
- [loguru-discord](https://pypi.org/project/loguru-discord/) - Loguru sink that posts logs to a webhook (last activity 2026-01).
- [python-discord/metricity](https://github.com/python-discord/metricity) - Metric collection used on the Python Discord server (last activity 2024-09).

### Miscellaneous

- [Skelmis/Discord-Anti-Spam](https://github.com/Skelmis/Discord-Anti-Spam) - Automatic spam handling for commands and messages (last activity 2026-07).
- [YousefEZ/discord-qalib](https://github.com/YousefEZ/discord-qalib) - XML templates for embeds and paginated menus (last activity 2026-01).
- [CasuallyCalm/discord-pretty-help](https://github.com/CasuallyCalm/discord-pretty-help) - Embed-based replacement for the built-in help command (last activity 2023-07).
- [mahtoid/DiscordChatExporterPy](https://github.com/mahtoid/DiscordChatExporterPy) - Export channel history to HTML transcripts (last activity 2026-05).
- [Bluenix2/discord-typings](https://github.com/Bluenix2/discord-typings) - TypedDicts for Discord gateway and HTTP payloads (last activity 2025-04).

### Templates

- [kkrypt0nn/Python-Discord-Bot-Template](https://github.com/kkrypt0nn/Python-Discord-Bot-Template) - Starter project for a personalized bot (last activity 2026-03).
- [PaulMarisOUMary/Discord-Bot](https://github.com/PaulMarisOUMary/Discord-Bot) - 2.x starter with hybrid commands, Docker, logging, and a database (last activity 2026-08).

## Example Bots

### Reference implementations

- [Rapptz/RoboDanny](https://github.com/Rapptz/RoboDanny) - Rapptz's production bot; commonly used as a reference implementation (last activity 2026-06).
- [AlexFlipnote/discord_bot](https://github.com/AlexFlipnote/discord_bot.py) - Minimal starter bot (last activity 2025-03).
- [avizum/alpine](https://github.com/avizum/alpine) - Public source for a general-purpose bot; author recommends the hosted instance (last activity 2026-08).
- [AbstractUmbra/Mipha](https://github.com/AbstractUmbra/Mipha) - Umbra's personal bot, forked from RoboDanny and kept on latest library releases (last activity 2026-07).
- [DuckBot-Discord/DuckBot](https://github.com/DuckBot-Discord/DuckBot) - Feature-rich bot with PostgreSQL and a documented local setup (last activity 2026-02).
- [Kile/Killua](https://github.com/Kile/Killua) - Games, moderation, and todo lists, plus extra algorithm notes in-tree (last activity 2026-08).
- [onerandomusername/monty-python](https://github.com/onerandomusername/monty-python) - Helper bot for Python project development (last activity 2026-02).

### Community and moderation

- [python-discord/bot](https://github.com/python-discord/bot) - Moderation, utils, and community tools for Python Discord (last activity 2026-08).
- [python-discord/sir-lancebot](https://github.com/python-discord/sir-lancebot) - On-ramp bot for new open-source contributors at Python Discord (last activity 2026-08).
- [DeJayDev/speedboat](https://github.com/DeJayDev/speedboat) - Tools for running large community servers (last activity 2024-09).
- [fourjr/rainbot](https://github.com/fourjr/rainbot) - Moderation bot with automod and logging (last activity 2026-04).
- [Tortoise-Community/tortoise-bot](https://github.com/Tortoise-Community/tortoise-bot) - Community bot for the Tortoise Discord (last activity 2026-08).
- [PythonistaGuild/Pythonista-Bot](https://github.com/PythonistaGuild/Pythonista-Bot) - Guild bot for the Pythonista Guild server (last activity 2025-02).
- [modmail-dev/Modmail](https://github.com/modmail-dev/Modmail) - Shared staff inbox, similar to Reddit Modmail (last activity 2026-08).
- [python-discord/sir-robin](https://github.com/python-discord/sir-robin) - Event-management bot for Python Discord (last activity 2026-07).

### Frameworks

- [Cog-Creators/Red-DiscordBot](https://github.com/Cog-Creators/Red-DiscordBot) - Self-hosted modular bot with a large cog ecosystem (last activity 2026-07).

### Music and games

- [ChocoMeow/Vocard](https://github.com/ChocoMeow/Vocard) - Music bot for YouTube, SoundCloud, Spotify, and Twitch (last activity 2026-07).
- [poketwo/poketwo](https://github.com/poketwo/poketwo) - Pokémon catching and collecting, in the Pokécord style (last activity 2025-02).
- [Ballsdex-Team/BallsDex-DiscordBot](https://github.com/Ballsdex-Team/BallsDex-DiscordBot) - Collect and trade countryballs (last activity 2026-08).
- [cheran-senthil/TLE](https://github.com/cheran-senthil/TLE) - Competitive programming helper for Codeforces and similar sites (last activity 2026-03).
- [jakobdylanc/llmcord](https://github.com/jakobdylanc/llmcord) - LLM frontend for OpenAI-compatible APIs inside a Discord server (last activity 2026-08).
- [statch/gitbot](https://github.com/statch/gitbot) - GitHub notifications and developer tools inside Discord (last activity 2026-08).
- [MikeyUsersREC/ERM](https://github.com/MikeyUsersREC/ERM) - Staff tools aimed at Roblox communities (last activity 2026-06).
- [Hunter87ff/Spruce](https://github.com/Hunter87ff/Spruce) - Tournament and server management (last activity 2026-08).

### Multipurpose

- [joinemm/miso-bot](https://github.com/joinemm/miso-bot) - General-purpose bot with Last.fm and K-pop commands (last activity 2026-06).
- [ZRunner/Axobot](https://github.com/Axobot-org/Axobot) - Multilingual general-purpose bot with moderation, XP, and Minecraft lookups (last activity 2026-08).
- [wasi-master/wm_bot](https://github.com/wasi-master/wm_bot) - General-purpose bot with a large command set (last activity 2026-07).
- [DTS-11/PizzaHat](https://github.com/DTS-11/PizzaHat) - General-purpose bot with a public website and AGPL source (last activity 2026-05).
- [Nirlep5252/EpicBot](https://github.com/Nirlep5252/EpicBot) - General-purpose bot with a large public command set (last activity 2025-07).

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

- [InterStella0/HelpCommand walkthrough](https://gist.github.com/InterStella0/b78488fb28cadf279dfd3164b9f0cf96) - Walkthrough for subclassing HelpCommand (last activity 2025-12).
- [Gobot1234/Sub-classing Help](https://gist.github.com/Gobot1234/45cad24df63fc144e85a7f8c85812567) - Guide to subclassing the help command (last activity 2021-07).
- [nonchris/Custom Help Command](https://gist.github.com/nonchris/1c7060a14a9d94e7929aa2ef14c41bc2) - Advanced custom help command example (last activity 2024-08).
- [voidoak/Implementing Help](https://gist.github.com/voidoak/4f34922888eeca04e1bba8c0ebd2f948) - Tutorial on implementing your own help command (last activity 2026-03).
- [Rapptz/Embed Help Command](https://gist.github.com/Rapptz/31a346ed1eb545ddeb0d451d81a60b3b) - Embed-based help command example from the library author (last activity 2024-07).

### Error Handling

- [Jeftaei/AppCommandErrorhandler.py](https://gist.github.com/Jeftaei/d0bad5044f1192a4c454f95a6b591d53) - Error handler covering prefix and app commands (last activity 2023-05).
- [EvieePy/Error Handling](https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612) - Error handling for prefix and app commands (last activity 2026-02).
- [irregularunit/Command Error Handler](https://gist.github.com/irregularunit/0221164777a476c653e36b49439b7b06) - Structured command error handler example (last activity 2023-07).

### Components and UI

- [esmaycat/Message Components](https://gist.github.com/esmaycat/500eafdad0aaf278b94c612764688976) - Using message components in 2.0 (last activity 2025-02).
- [lykn/Buttons](https://gist.github.com/lykn/bac99b06d45ff8eed34c2220d86b6bf4) - How to make buttons in v2 (last activity 2026-02).
- [lykn/Selects or Dropdowns](https://gist.github.com/lykn/a2b68cb790d6dad8ecff75b2aa450f23) - Select menus in v2 (last activity 2026-01).
- [Soheab/Simple Button Paginator](https://gist.github.com/Soheab/f226fc06a3468af01ea3168c95b30af8) - Small paginator with three buttons (last activity 2026-04).
- [InterStella0/Pagination Walkthrough](https://gist.github.com/InterStella0/454cc51e05e60e63b81ea2e8490ef140) - Walkthrough of action-based pagination (last activity 2025-04).
- [mikeshardmind/List Menu](https://gist.github.com/mikeshardmind/bff6f937032455d83b8f1724ef73575a) - List menu pagination snippet (last activity 2024-03).
- [imptype/Message Maker](https://gist.github.com/imptype/7b35c6769684fb68178e5719e5f81b6d) - Embed/message builder command (last activity 2025-03).
- [quackbarc/2.0 Paginators](https://gist.github.com/quackbarc/31e5cd789d232ad0d263511bb1a506e8) - Paginator examples for 2.0 (last activity 2022-03).
- [Soheab/wait_for Modal](https://gist.github.com/Soheab/f46fee27498aad4a8962d59b6f0415c6) - Wait for user input with a modal (last activity 2024-11).
- [Soheab/Global View](https://gist.github.com/Soheab/cfd769870b7b6eaf00a7aebf5293a622) - Pattern for a globally registered view (last activity 2026-04).

### Components V2

- [Soheab/Components V2 to LayoutView](https://gist.github.com/Soheab/ab7a833725f95a84a8f7fa17995cb36c) - Mapping Components V2 to LayoutView (last activity 2026-07).
- [Soheab/CV2 Paginator](https://gist.github.com/Soheab/891c39d7294b1bdbadc7ecf35ce51cc5) - Components V2 paginator (last activity 2026-04).
- [Soheab/Embed to Container](https://gist.github.com/Soheab/cf356c62a6134508869bf40640b04856) - Convert an embed into a Components V2 container (last activity 2025-11).

### Cogs and Commands

- [LeoCx1000/MentionableTree implementation](https://gist.github.com/LeoCx1000/021dc52981299b95ea7790416e4f5ca4) - Mentionable CommandTree so slash commands can be mentioned (last activity 2025-05).
- [Ikusaba-san/Cog Methods](https://gist.github.com/Ikusaba-san/69115b79d33e05ed07ec4a4f14db83b1) - List of special cog methods (last activity 2021-05).
- [Painezor/Checks](https://gist.github.com/Painezor/eb2519022cd2c907b56624105f94b190) - Built-in checks for the commands extension (last activity 2025-04).
- [Samarthh2601/App Commands Walkthrough](https://gist.github.com/Samarthh2601/b6f57065f394b54f43666037ade38d32) - Walkthrough for application commands (last activity 2025-01).
- [EvieePy/Cogs Example](https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be) - Classic cogs and extension layout (last activity 2025-08).
- [Soheab/self.bot in Cogs](https://gist.github.com/Soheab/cf387b753da32eb02f3228c2e32bb03f) - How `self.bot` works inside a cog (last activity 2026-08).
- [Soheab/wait_for in Commands](https://gist.github.com/Soheab/e73ab6f66881ee4102be37815da3a24e) - Examples of `wait_for` inside ext.commands (last activity 2025-06).
- [Soheab/Any-Permission Check](https://gist.github.com/Soheab/ec3f40f9f54add0dba787783719331f8) - Custom check that passes if the user has any of the given permissions (last activity 2024-07).

### Other Snippets

- [scragly/Learning discord.py](https://gist.github.com/scragly/095b5278a354d46e86f02d643fc3d64b) - Setup, core concepts, and a resource list for learning the library (last activity 2025-12).
- [advaith1/Intents Explainer](https://gist.github.com/advaith1/e69bcc1cdd6d0087322734451f15aa2f) - Gateway and privileged intents: statuses, members, and message content (last activity 2026-02).
- [cibere/Defer Response](https://gist.github.com/cibere/7e1356575780e716d2e3a23ea2bcf6da) - Acknowledge an interaction and respond later, up to 15 minutes (last activity 2025-02).
- [mikeshardmind/SQLite Examples](https://gist.github.com/mikeshardmind/d7d2c6cb19b53ab76b7d401b2716df5d) - Common SQLite patterns for bots (last activity 2025-08).
- [AkshuAgarwal/Interactions](https://gist.github.com/AkshuAgarwal/bc7d45bcecd5d29de4d6d7904e8b8bd8) - Intro to interactions and how to handle them (last activity 2026-02).
- [CuteFwan/wait_for Multiple Events](https://gist.github.com/CuteFwan/ded1bf520d71baac18726fa2e0554f0f) - Waiting for more than one Discord event at a time (last activity 2021-08).
- [kkrypt0nn/ANSI Colors on Discord](https://gist.github.com/kkrypt0nn/a02506f3712ff2d1c8ca7c9e0aed7c06) - ANSI color codes in Discord code blocks (last activity 2026-08).
- [LeviSnoot/Discord Timestamps](https://gist.github.com/LeviSnoot/d9147767abeef2f770e9ddcd91eb85aa) - Discord timestamp markdown syntax (last activity 2026-07).
- [4Kaylum/Discord.py Tutorial](https://gist.github.com/4Kaylum/a1e9f31c31b17386c36f017d3c59cdcc) - Simple bot tutorial (last activity 2026-05).
- [philskillz-coder/Color Transformer](https://gist.github.com/philskillz-coder/c6bee6c8e258ad56afb01840df26a1fa) - Color transformer and autocomplete (last activity 2023-06).
- [Soheab/Threads](https://gist.github.com/Soheab/4709e335474784d8a1877812f6d0c354) - Creating and managing Discord threads (last activity 2026-07).
- [Soheab/Voice Channel Status](https://gist.github.com/Soheab/e9a747f5c8fae43447a5611e483b4beb) - React when a voice channel status is set or changed (last activity 2026-02).
- [Soheab/No Message Content Intent Ideas](https://gist.github.com/Soheab/a6229dbbe3acf3ce9a4625bf9e7177da) - Command ideas that work without the privileged message content intent (last activity 2025-12).
- [Soheab/discord.Colour](https://gist.github.com/Soheab/d9cf3f40e34037cfa544f464fc7d919e) - Reference for discord.Colour helpers (last activity 2026-02).
- [Soheab/APIs for Discord Bots](https://gist.github.com/Soheab/332ba85f8989648449c71bdc8ef32368) - Community list of APIs commonly used with Discord bots (last activity 2026-08).
- [Soheab/Server Tag](https://gist.github.com/Soheab/d5e7fdbca3db94629cf87f1178096aab) - Overflow copy of a long official-server tag that exceeded Discord's character limit (last activity 2024-10).

## Additional Resources

- [Permissions Calculator](https://discordapi.com/permissions.html) - Build bot invite links with a chosen permission bitfield.
- [Discord Community Resources](https://discord.com/developers/docs/topics/community-resources) - Official index of libraries, calculators, and embed tools.
- [Intent Calculator](https://ziad87.net/intents/) - Build a gateway intents bitfield for Identify.
- [Embed Visualizer](https://leovoel.github.io/embed-visualizer/) - Live embed designer with generated library snippets.
- [discord-interactions-python](https://github.com/discord/discord-interactions-python) - Official helpers for verifying HTTP interaction signatures (last activity 2024-04).
- [Soheab/dpy-missing-features](https://github.com/Soheab/dpy-missing-features) - Discord API features the library does not yet expose (last activity 2024-08).
- [Soheab/discord.py-tags](https://github.com/Soheab/discord.py-tags) - Overflow copies of long tags from the official library Discord (last activity 2024-12).
- [Soheab/dpy-badhosts](https://github.com/Soheab/dpy-badhosts) - Hosts the community generally warns against using for bots (last activity 2024-11).
- [Rapptz/asqlite](https://github.com/Rapptz/asqlite) - Async wrapper around sqlite3 (last activity 2024-07).

## Forks and Wrappers

disnake, nextcord, Novus, pycord, and discord.py-message-components are discord.py forks. hikari, hata, interactions.py, and discord.http are independent wrappers, not drop-in replacements for discord.py.

- [disnake](https://github.com/DisnakeDev/disnake) - Async Discord API wrapper, forked from discord.py (last activity 2026-08).
- [nextcord](https://github.com/nextcord/nextcord) - API wrapper forked from discord.py (last activity 2026-08).
- [Novus](https://github.com/Voxel-Fox-Ltd/Novus) - Async API wrapper forked from discord.py, used by VoxelBotUtils (last activity 2026-07).
- [pycord](https://github.com/Pycord-Development/pycord) - Maintained fork of discord.py (last activity 2026-08).
- [mccoderpy/discord.py-message-components](https://github.com/mccoderpy/discord.py-message-components) - Fork that added message components before they landed upstream (last activity 2025-06).
- [hikari](https://github.com/hikari-py/hikari) - Independent async wrapper, not a drop-in replacement (last activity 2026-08).
- [interactions.py](https://github.com/interactions-py/interactions.py) - Independent bot framework, not a drop-in replacement (last activity 2026-08).
- [hata](https://github.com/HuyaneMatsu/hata) - Independent async wrapper, not a drop-in replacement (last activity 2026-08).
- [AlexFlipnote/discord.http](https://github.com/AlexFlipnote/discord.http) - HTTP-interactions-first library with optional gateway and cache control (last activity 2026-08).

## Related

- [awesome-discord-communities](https://github.com/mhxion/awesome-discord-communities) - Programmer Discord communities (last activity 2026-04).
- [jacc/awesome-discord](https://github.com/jacc/awesome-discord) - Clients, bots, libraries, and related tools (last activity 2026-05).
- [Discord Library Comparison](https://libs.advaith.io) - Feature matrix across Discord libraries.

<!-- END CONTENT -->

## Contributing

[Contributions of any kind welcome, just follow the guidelines](contributing.md)!

### Contributors

[Thanks goes to these contributors](https://github.com/kzndotsh/awesome-discordpy/graphs/contributors)!
