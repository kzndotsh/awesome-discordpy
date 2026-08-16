<!-- title -->

<!--lint ignore no-dead-urls-->
<!--lint disable awesome-heading-->
# Awesome Discord.py List

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![lint](https://github.com/kzndotsh/awesome-discordpy/actions/workflows/lint.yaml/badge.svg)](https://github.com/kzndotsh/awesome-discordpy/actions/workflows/lint.yaml)

<!-- subtitle -->

An Awesome list for all things Discord.py

<!-- image -->

![Discord.py Logo](assets/banner.png)

<!-- description -->

[Discord.py](https://discordpy.readthedocs.io/en/stable/) is a modern, easy to use, feature-rich, and async ready API wrapper for Discord.

<!-- TOC -->

## Contents

<!--lint disable awesome-toc-->
- [Awesome Discord.py List](#awesome-discordpy-list)
  - [Contents](#contents)
  - [Official Links](#official-links)
  - [Libraries and Extensions](#libraries-and-extensions)
    - [Utilities](#utilities)
    - [Testing and Debugging](#testing-and-debugging)
    - [UI - Pagination, Menus, Embeds and similar](#ui---pagination-menus-embeds-and-similar)
    - [Inter-Process Communication](#inter-process-communication)
    - [Voice and Audio](#voice-and-audio)
    - [Authentication](#authentication)
    - [Metrics, Monitoring, and Logging](#metrics-monitoring-and-logging)
    - [Miscellaneous](#miscellaneous)
    - [Templates](#templates)
  - [Example Bots](#example-bots)
  - [Blog Posts, Guides and Tutorials](#blog-posts-guides-and-tutorials)
  - [Community Gists and Snippets](#community-gists-and-snippets)
    - [Help Commands](#help-commands)
    - [Error Handling](#error-handling)
    - [Components and UI](#components-and-ui)
    - [Components V2](#components-v2)
    - [Other Snippets](#other-snippets)
  - [Additional Resources](#additional-resources)
  - [Forks and Wrappers](#forks-and-wrappers)
  - [Archived/Deprecated](#archiveddeprecated)
  - [Contributing](#contributing)
    - [Contributors](#contributors)

<!-- CONTENT -->

## Official Links

- [Discord.py Documentation](https://discordpy.readthedocs.io/en/latest/) - Official documentation for Discord.py.
- [Discord.py Changelog](https://discordpy.readthedocs.io/en/latest/whats_new.html) - Official changelog for Discord.py.
- [Discord.py FAQ](https://discordpy.readthedocs.io/en/latest/faq.html) - Official frequently asked questions for discord.py.
- [Migrating to v2.0](https://discordpy.readthedocs.io/en/latest/migrating.html) - Official breaking-change guide for discord.py 2.0.
- [Discord.py Quickstart](https://discordpy.readthedocs.io/en/latest/quickstart.html) - Official getting-started guide.
- [Official Examples](https://github.com/Rapptz/discord.py/tree/master/examples) - Example bots and snippets from the discord.py repository (last activity 2026-07).
- [Discord.py GitHub](https://github.com/Rapptz/discord.py) - Official GitHub repository for Discord.py (last activity 2026-07).
- [Discord.py Discord Server](https://discord.gg/dpy) - Official Discord server for Discord.py.

## Libraries and Extensions

### Utilities

- [InterStella0/starlight-dpy](https://github.com/InterStella0/starlight-dpy) - A utility library for discord.py (last activity 2024-02).
- [clari7744/DPyUtils](https://github.com/clari7744/DPyUtils) - Some extra discord.py additions such as duration utilities, converters, a context editor and more (last activity 2026-04).
- [tanrbobanr/dpy-check](https://github.com/tanrbobanr/dpy-check) - A system for making more dynamic and complex checks on discord.py commands (last activity 2023-01).
- [cogwatch](https://pypi.org/project/cogwatch/) - Hot-reloading for discord.py-based command files.
- [timelessnesses/dpyhr](https://github.com/timelessnesses/dpyhr) - Dpyhr is a hot cog reloader (that uses discord.py cog's implementation) to reload anytime you wanted to save (last activity 2023-04).
- [mikeshardmind/discord-scheduler](https://github.com/mikeshardmind/discord-scheduler) - A persistent scheduling implementation suitable for use with discord.py (last activity 2025-02).
- [Voxel-Fox-Ltd/VoxelBotUtils](https://github.com/Voxel-Fox-Ltd/VoxelBotUtils) - An extension of discord.py that adds helpers for bot setup, commands, and common patterns (last activity 2024-01).
- [Kyrela/discore](https://github.com/Kyrela/discore) - A small core for initializing discord.py bots and tracking logs and errors (last activity 2026-01).
- [Soheab/discord.py-listen-overloads](https://github.com/Soheab/discord.py-listen-overloads) - Type stubs that add overloads to `@commands.Bot.listen` for discord.py events (last activity 2023-12).
- [Soheab/discord-ext-subcommands](https://github.com/Soheab/discord-ext-subcommands) - Define prefix, slash, and hybrid subcommands across multiple files and cogs (last activity 2026-03).
- [Soheab/discord-ext-custom_interaction](https://github.com/Soheab/discord-ext-custom_interaction) - Subclass `discord.Interaction` to add helpers such as `send` and `author` (last activity 2025-01).
- [tibue99/ezcord](https://github.com/tibue99/ezcord) - An easy-to-use extension for Discord.py and Pycord (last activity 2026-07).

### Testing and Debugging

- [scarletcafe/jishaku](https://github.com/scarletcafe/jishaku) - A debugging and testing cog for discord.py rewrite bots (last activity 2026-04).
- [CraftSpider/dpytest](https://github.com/CraftSpider/dpytest) - A package that assists in writing tests for discord.py (last activity 2026-06).

### UI - Pagination, Menus, Embeds and similar

- [Defxult/reactionmenu](https://github.com/Defxult/reactionmenu) - A library to create a discord.py 2.0+ paginator. Supports pagination with buttons, reactions, and category selection using selects (last activity 2026-05).
- [Soheab/discord-py-paginators](https://github.com/Soheab/discord-py-paginators) - An extension for discord.py that provides various paginators (last activity 2025-10).
- [Soheab/modal-paginator](https://github.com/Soheab/modal-paginator) - An extension for discord.py that allows you to paginate a Modal using buttons (last activity 2025-05).
- [philskillz-coder/discord-py-paginator](https://github.com/philskillz-coder/discord-py-paginator) - A view paginator for discord.py (last activity 2025-04).
- [thegamecracks/discord-ext-pager](https://github.com/thegamecracks/discord-ext-pager) - A discord.py 2.0 paginator library with a similar interface to discord-ext-menus (last activity 2026-08).
- [OnceYT/dpy-paginator](https://github.com/OnceYT/dpy-paginator) - A discord.py utility with no external dependencies that makes paginating embeds easier (last activity 2024-10).
- [Soheab/discord-ext-embeds](https://github.com/Soheab/discord-ext-embeds) - An extension for discord.py that adds a few nice-to-have features to discord.py's embed (last activity 2025-03).
- [keizaiya/discord-ext-flow](https://github.com/keizaiya/discord-ext-flow) - This library extends discord.ui, providing UI control based on state flows (last activity 2026-08).
- [sizumita/discord-ext-ui](https://github.com/sizumita/discord-ext-ui) - An extension of discord-ui that adds some quality-of-life features (last activity 2024-10).
- [Seniatical/dpy-paginator](https://github.com/Seniatical/dpy-paginator) -  A simple pagination library for discord.py, comes with support for dropdown, button based pagination (last activity 2023-04).
- [vcv88/discord-ext-dyn](https://github.com/vcv88/discord-ext-dyn) - An extension for handling dynamic modals/buttons/select menus (last activity 2024-01).
- [Modern-Realm/discord_btns_menus](https://github.com/Modern-Realm/discord_btns_menus) - Helpers for buttons, select menus, combinations, and pagination on discord.py and related forks (last activity 2024-06).
- [HollowTheSilver/CascadeUI](https://github.com/HollowTheSilver/CascadeUI) - A Redux-inspired UI framework for discord.py with Components V2, persistence, and pre-built patterns (last activity 2026-08).
- [LiBa001/disputils](https://github.com/LiBa001/disputils) - Pagination, confirmation, and other small discord.py UI utilities (last activity 2024-05).

### Inter-Process Communication

- [No767/discord-ext-ipcx](https://github.com/No767/discord-ext-ipcx) - An maintained discord.py extension for inter-process communication (last activity 2026-08).

### Voice and Audio

- [discord-ext-voice-recv](https://github.com/imayhaveborkedit/discord-ext-voice-recv) - Voice receive extension package for discord.py (last activity 2025-06).
- [Sheppsu/discord-ext-listening](https://github.com/Sheppsu/discord-ext-listening) - Voice receive extension for discord.py built on multiprocessing and designed to be flexible (last activity 2024-02).
- [PythonistaGuild/Wavelink](https://github.com/PythonistaGuild/Wavelink) - A fully asynchronous Lavalink v4 wrapper built for discord.py (last activity 2026-07).
- [devoxin/Lavalink.py](https://github.com/devoxin/Lavalink.py) - A powerful, intuitive Python wrapper for Lavalink (last activity 2026-06).
- [cloudwithax/pomice](https://github.com/cloudwithax/pomice) - A modern Lavalink wrapper for discord.py with Spotify and Apple Music querying (last activity 2026-07).
- [ooliver1/mafic](https://github.com/ooliver1/mafic) - A typed Lavalink client for discord.py and related forks (last activity 2026-08).
- [PyLav/PyLav](https://github.com/PyLav/PyLav) - A Lavalink wrapper aimed at discord.py bots, including Red-DiscordBot (last activity 2026-08).

### Authentication

- [treeben77/discord-oauth2.py](https://github.com/treeben77/discord-oauth2.py) - API Wrapper for Discord OAuth2 & Linked Roles in Python (last activity 2026-01).
- [Soheab/oauthcord.py](https://github.com/Soheab/oauthcord.py) - An async Discord OAuth2 client with typed REST models. Not a bot framework (last activity 2026-08).

### Metrics, Monitoring, and Logging

- [discord-ext-prometheus](https://github.com/ApolloRoboto/discord.py-ext-prometheus) - An extension for the discord.py library that enables Prometheus metrics (last activity 2025-02).
- [loguru-discord](https://pypi.org/project/loguru-discord/) - Lightweight sink for Loguru that sends logs to Discord via webhook (last activity 2026-01).
- [python-discord/metricity](https://github.com/python-discord/metricity) - Advanced metric collection for the Python Discord server (last activity 2024-09).

### Miscellaneous

- [Skelmis/Discord-Anti-Spam](https://github.com/Skelmis/Discord-Anti-Spam) - DPY Anti-Spam is a package aimed to handle all required logic under the hood for handling spammers (last activity 2026-07).
- [YousefEZ/discord-qalib](https://github.com/YousefEZ/discord-qalib) - Discord library built on discord.py to simplify source code by rendering markup (xml) templates of embeds and menus (Pagination) (last activity 2026-01).
- [CasuallyCalm/discord-pretty-help](https://github.com/CasuallyCalm/discord-pretty-help) - An embed version of the built in help command for discord.py (last activity 2023-07).
- [mahtoid/DiscordChatExporterPy](https://github.com/mahtoid/DiscordChatExporterPy) - Export Discord channel chats to HTML transcripts from a discord.py bot (last activity 2026-05).
- [Bluenix2/discord-typings](https://github.com/Bluenix2/discord-typings) - TypedDict typings for Discord API payloads (last activity 2025-04).

### Templates

- [kkrypt0nn/Python-Discord-Bot-Template](https://github.com/kkrypt0nn/Python-Discord-Bot-Template) - A simple, actively maintained template for starting a personalized discord.py bot (last activity 2026-03).
- [PaulMarisOUMary/Discord-Bot](https://github.com/PaulMarisOUMary/Discord-Bot) - An advanced discord.py 2.x starter with hybrid commands, Docker, logging, and database support (last activity 2026-08).

## Example Bots

- [Rapptz/RoboDanny](https://github.com/Rapptz/RoboDanny) - A Discord bot written by Rapptz, the creator of discord.py (last activity 2026-06).
- [statch/gitbot](https://github.com/statch/gitbot) - GitBot is a programmer toolkit for developers to stay productive and connect with their friends on GitHub right from Discord (last activity 2026-08).
- [python-discord/bot](https://github.com/python-discord/bot) - The community bot for the Python Discord community (last activity 2026-08).
- [DeJayDev/speedboat](https://github.com/DeJayDev/speedboat) - A Discord bot for managing large communities (last activity 2024-09).
- [joinemm/miso-bot](https://github.com/joinemm/miso-bot) - Miso is a multipurpose Discord bot with over 100 commands and features (last activity 2026-06).
- [AlexFlipnote/discord_bot](https://github.com/AlexFlipnote/discord_bot.py) - A simple Discord bot that helps you getting started within discord.py (last activity 2025-03).
- [ZRunner/Axobot](https://github.com/Axobot-org/Axobot) - A cool multipurpose Discord bot made in Python (last activity 2026-08).
- [MikeyUsersREC/ERM](https://github.com/MikeyUsersREC/ERM) - A Discord bot primarily focused on improving the Roblox staff experience (last activity 2026-06).
- [Hunter87ff/Spruce](https://github.com/Hunter87ff/Spruce) - Spruce is a multi-functional open source Discord bot, designed to streamline the management of Discord tournaments and servers (last activity 2026-08).
- [poketwo/poketwo](https://github.com/poketwo/poketwo) - A Pokémon-oriented Discord bot that lets you collect pokémon. Catch pokémon in the wild, level your pokémon, compete with your friends, and more (last activity 2025-02).
- [wasi-master/wm_bot](https://github.com/wasi-master/wm_bot) - A multipurpose Discord bot with more than 220 commands (last activity 2026-07).
- [DuckBot-Discord/DuckBot](https://github.com/DuckBot-Discord/DuckBot) - Source for DuckBot, a feature-rich discord.py bot with PostgreSQL and a documented local setup (last activity 2026-02).
- [DTS-11/PizzaHat](https://github.com/DTS-11/PizzaHat) - A multi-purpose discord.py bot with a public website and AGPL source (last activity 2026-05).
- [avizum/alpine](https://github.com/avizum/alpine) - A discord.py bot kept as a public reference implementation (last activity 2026-08).
- [Nirlep5252/EpicBot](https://github.com/Nirlep5252/EpicBot) - A simple, multipurpose discord.py bot with a large public command set (last activity 2025-07).
- [Kile/Killua](https://github.com/Kile/Killua) - Source for Killua, a maintained discord.py bot with extra algorithm notes in-tree (last activity 2026-08).
- [Cog-Creators/Red-DiscordBot](https://github.com/Cog-Creators/Red-DiscordBot) - A modular, multi-function discord.py bot framework with a large cog ecosystem (last activity 2026-07).
- [modmail-dev/Modmail](https://github.com/modmail-dev/Modmail) - A staff shared-inbox bot for Discord, similar to Reddit Modmail (last activity 2026-08).
- [python-discord/sir-lancebot](https://github.com/python-discord/sir-lancebot) - Python Discord's community bot for newer open-source contributors (last activity 2026-08).
- [ChocoMeow/Vocard](https://github.com/ChocoMeow/Vocard) - A user-friendly discord.py music bot with YouTube, SoundCloud, Spotify, and Twitch support (last activity 2026-07).
- [cheran-senthil/TLE](https://github.com/cheran-senthil/TLE) - A discord.py bot for competitive programming on Codeforces and similar sites (last activity 2026-03).
- [jakobdylanc/llmcord](https://github.com/jakobdylanc/llmcord) - A discord.py bot that turns Discord into a collaborative LLM frontend (last activity 2026-08).
- [Ballsdex-Team/BallsDex-DiscordBot](https://github.com/Ballsdex-Team/BallsDex-DiscordBot) - Collect-and-trade countryballs bot written with discord.py (last activity 2026-08).
- [onerandomusername/monty-python](https://github.com/onerandomusername/monty-python) - A discord.py bot for helping with Python project development (last activity 2026-02).
- [AbstractUmbra/Mipha](https://github.com/AbstractUmbra/Mipha) - Umbra's personal discord.py bot, useful as a modern reference implementation (last activity 2026-07).
- [PythonistaGuild/Pythonista-Bot](https://github.com/PythonistaGuild/Pythonista-Bot) - The discord.py bot for the Pythonista Guild server (last activity 2025-02).
- [fourjr/rainbot](https://github.com/fourjr/rainbot) - A discord.py moderation bot with automod and logging (last activity 2026-04).
- [Tortoise-Community/tortoise-bot](https://github.com/Tortoise-Community/tortoise-bot) - A fully featured discord.py community bot (last activity 2026-08).

## Blog Posts, Guides and Tutorials

- [User Installable Applications - Umbra's Rantings](https://about.abstractumbra.dev/discord.py/2024/04/11/user-installable-applications.html) - This post is all about User Installable Applications and how to set them up.
- [All about selects - Umbra's Rantings](https://about.abstractumbra.dev/discord.py/2023/09/25/selects.html) - This post is about the different types of select menus and how to use them.
- [Application Command definition examples - Umbra's Rantings](https://about.abstractumbra.dev/discord.py/2023/01/30/app-command-examples.html) - This post is about the different types of application commands and how to use them.
- [Application command basics - Umbra's Rantings](https://about.abstractumbra.dev/discord.py/2023/01/30/app-command-basics.html) - In this guide, you'll cover everything from regular ol' slash commands all the way to Modals and the other component goodies.
- [Umbra's Sync Command - Umbra's Rantings](https://about.abstractumbra.dev/discord.py/2023/01/29/sync-command-example.html) - A full featured command and explanation for syncing your CommandTree.
- [Discord.py Masterclass](https://fallendeity.github.io/discord.py-masterclass/) - A tutorial/guide explaining all features in discord.py and how to make a Discord bot from scratch.
- [Python Discord - Discord.py Learning Guide](https://www.pythondiscord.com/pages/guides/python-guides/discordpy/) - A curated learning path covering bot setup, commands, FAQ, and commonly cited community examples.
- [Components V2 - Umbra's Rantings](https://about.abstractumbra.dev/discord.py/2025/08/17/components-v2.html) - Guide to discord.py 2.6 LayoutView and Discord's Components V2 system.

## Community Gists and Snippets

### Help Commands

- [InterStella0/HelpCommand walkthrough](https://gist.github.com/InterStella0/b78488fb28cadf279dfd3164b9f0cf96) - Walkthrough for subclassing discord.py's HelpCommand (last activity 2025-12).
- [Gobot1234/Sub-classing Help](https://gist.github.com/Gobot1234/45cad24df63fc144e85a7f8c85812567) - Guide to subclassing the help command in discord.py (last activity 2021-07).
- [nonchris/Custom Help Command](https://gist.github.com/nonchris/1c7060a14a9d94e7929aa2ef14c41bc2) - An advanced custom help command example for discord.py bots (last activity 2024-08).
- [voidoak/Implementing Help](https://gist.github.com/voidoak/4f34922888eeca04e1bba8c0ebd2f948) - Tutorial on implementing your own help command in discord.py (last activity 2026-03).
- [Rapptz/Embed Help Command](https://gist.github.com/Rapptz/31a346ed1eb545ddeb0d451d81a60b3b) - Embed-based help command example from the discord.py author (last activity 2024-07).

### Error Handling

- [Jeftaei/AppCommandErrorhandler.py](https://gist.github.com/Jeftaei/d0bad5044f1192a4c454f95a6b591d53) - A robust error handler for discord.py commands, including app commands (last activity 2023-05).
- [EvieePy/Error Handling](https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612) - Error handling for prefix and app commands in discord.py (last activity 2026-02).
- [irregularunit/Command Error Handler](https://gist.github.com/irregularunit/0221164777a476c653e36b49439b7b06) - Structured command error handler example for discord.py (last activity 2023-07).

### Components and UI

- [esmaycat/Message Components](https://gist.github.com/esmaycat/500eafdad0aaf278b94c612764688976) - This gist shows you how to use message components in discord.py 2.0 (last activity 2025-02).
- [lykn/Buttons](https://gist.github.com/lykn/bac99b06d45ff8eed34c2220d86b6bf4) - A gist which shows/tells you how to make buttons using discord.py v2 (last activity 2026-02).
- [lykn/Selects or Dropdowns](https://gist.github.com/lykn/a2b68cb790d6dad8ecff75b2aa450f23) -  A gist explaining the right way to make drop down menus/select menus/selects in discord.py v2 (last activity 2026-01).
- [Soheab/Simple Button Paginator](https://gist.github.com/Soheab/f226fc06a3468af01ea3168c95b30af8) - A small paginator with three buttons (last activity 2026-04).
- [InterStella0/Pagination Walkthrough](https://gist.github.com/InterStella0/454cc51e05e60e63b81ea2e8490ef140) - Walkthrough of action-based pagination in discord.py (last activity 2025-04).
- [mikeshardmind/List Menu](https://gist.github.com/mikeshardmind/bff6f937032455d83b8f1724ef73575a) - List menu pagination snippet for discord.py (last activity 2024-03).
- [imptype/Message Maker](https://gist.github.com/imptype/7b35c6769684fb68178e5719e5f81b6d) - An embed/message builder command for discord.py (last activity 2025-03).
- [quackbarc/2.0 Paginators](https://gist.github.com/quackbarc/31e5cd789d232ad0d263511bb1a506e8) - Paginator examples for discord.py 2.0 (last activity 2022-03).
- [Soheab/wait_for Modal](https://gist.github.com/Soheab/f46fee27498aad4a8962d59b6f0415c6) - Wait for user input with a modal in discord.py (last activity 2024-11).
- [Soheab/Global View](https://gist.github.com/Soheab/cfd769870b7b6eaf00a7aebf5293a622) - Pattern for a globally registered discord.py view (last activity 2026-04).

### Components V2

- [Soheab/Components V2 to LayoutView](https://gist.github.com/Soheab/ab7a833725f95a84a8f7fa17995cb36c) - Example of mapping Discord Components V2 to discord.py LayoutView (last activity 2026-07).
- [Soheab/CV2 Paginator](https://gist.github.com/Soheab/891c39d7294b1bdbadc7ecf35ce51cc5) - A Components V2 paginator for discord.py (last activity 2026-04).
- [Soheab/Embed to Container](https://gist.github.com/Soheab/cf356c62a6134508869bf40640b04856) - Convert a discord.py embed into a Components V2 container (last activity 2025-11).

### Other Snippets

- [scragly/Learning discord.py](https://gist.github.com/scragly/095b5278a354d46e86f02d643fc3d64b) - Comprehensive guide and resource list for learning and building Discord bots using discord.py, including setup, essential concepts, and examples (last activity 2025-12).
- [advaith1/Intents Explainer](https://gist.github.com/advaith1/e69bcc1cdd6d0087322734451f15aa2f) - If you're wondering what Gateway Intents are, what Privileged Intents are, why your bot can't see statuses, or why your bot can't see member joins anymore, then this page should explain it to you! (last activity 2026-02).
- [cibere/Defer Response](https://gist.github.com/cibere/7e1356575780e716d2e3a23ea2bcf6da) - The defer response, defers the interaction response. This is typically used when the interaction is acknowledged and an optional secondary action will be done later. When deferring, you get up to 15 minutes to respond instead of the normal 3 seconds (last activity 2025-02).
- [mikeshardmind/SQLite Examples](https://gist.github.com/mikeshardmind/d7d2c6cb19b53ab76b7d401b2716df5d) - "Common" Discord bot SQLite examples (last activity 2025-08).
- [AkshuAgarwal/Interactions](https://gist.github.com/AkshuAgarwal/bc7d45bcecd5d29de4d6d7904e8b8bd8) - A Basic guide about Discord Interactions and how to use them in discord.py (last activity 2026-02).
- [LeoCx1000/MentionableTree implementation](https://gist.github.com/LeoCx1000/021dc52981299b95ea7790416e4f5ca4) - Mentionable CommandTree implementation to allow mentioning slash commands in discord.py (last activity 2025-05).
- [Ikusaba-san/Cog Methods](https://gist.github.com/Ikusaba-san/69115b79d33e05ed07ec4a4f14db83b1) - A list of all special cog methods (last activity 2021-05).
- [Painezor/Checks](https://gist.github.com/Painezor/eb2519022cd2c907b56624105f94b190) - A list of built-in Checks for the commands extension of discord.py (last activity 2025-04).
- [CuteFwan/wait_for Multiple Events](https://gist.github.com/CuteFwan/ded1bf520d71baac18726fa2e0554f0f) - Example of waiting for multiple Discord events (last activity 2021-08).
- [Samarthh2601/App Commands Walkthrough](https://gist.github.com/Samarthh2601/b6f57065f394b54f43666037ade38d32) - Walkthrough for discord.py application commands (last activity 2025-01).
- [EvieePy/Cogs Example](https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be) - Classic cogs/extension layout example for discord.py rewrite (last activity 2025-08).
- [kkrypt0nn/ANSI Colors on Discord](https://gist.github.com/kkrypt0nn/a02506f3712ff2d1c8ca7c9e0aed7c06) - Guide to ANSI color codes in Discord code blocks (last activity 2026-08).
- [LeviSnoot/Discord Timestamps](https://gist.github.com/LeviSnoot/d9147767abeef2f770e9ddcd91eb85aa) - Discord timestamp markdown syntax reference (last activity 2026-07).
- [4Kaylum/Discord.py Tutorial](https://gist.github.com/4Kaylum/a1e9f31c31b17386c36f017d3c59cdcc) - A simple bot tutorial for discord.py (last activity 2026-05).
- [philskillz-coder/Color Transformer](https://gist.github.com/philskillz-coder/c6bee6c8e258ad56afb01840df26a1fa) - Color transformer and autocomplete for discord.py (last activity 2023-06).
- [Soheab/Threads](https://gist.github.com/Soheab/4709e335474784d8a1877812f6d0c354) - Guide to Discord threads and how to manage them with discord.py (last activity 2026-07).
- [Soheab/Voice Channel Status](https://gist.github.com/Soheab/e9a747f5c8fae43447a5611e483b4beb) - How to react when a voice channel status is set or changed (last activity 2026-02).
- [Soheab/No Message Content Intent Ideas](https://gist.github.com/Soheab/a6229dbbe3acf3ce9a4625bf9e7177da) - Command ideas that work without the privileged message content intent (last activity 2025-12).
- [Soheab/self.bot in Cogs](https://gist.github.com/Soheab/cf387b753da32eb02f3228c2e32bb03f) - Explains how `self.bot` works inside a discord.py cog (last activity 2026-08).
- [Soheab/wait_for in Commands](https://gist.github.com/Soheab/e73ab6f66881ee4102be37815da3a24e) - Examples of `wait_for` inside ext.commands (last activity 2025-06).
- [Soheab/Any-Permission Check](https://gist.github.com/Soheab/ec3f40f9f54add0dba787783719331f8) - A custom check that passes if the user has any of the given permissions (last activity 2024-07).
- [Soheab/discord.Colour](https://gist.github.com/Soheab/d9cf3f40e34037cfa544f464fc7d919e) - Reference for discord.Colour helpers and usage (last activity 2026-02).
- [Soheab/APIs for Discord Bots](https://gist.github.com/Soheab/332ba85f8989648449c71bdc8ef32368) - Community list of APIs commonly used with Discord bots (last activity 2026-08).

## Additional Resources

- [Permissions Calculator](https://discordapi.com/permissions.html) - Create invite links for bots with specific permissions.
- [Discord Community Resources](https://discord.com/developers/docs/topics/community-resources) - Official Discord docs index of libraries, permission/intent calculators, and embed tools.
- [Intent Calculator](https://ziad87.net/intents/) - Build a gateway intents bitfield for your Identify payload.
- [Embed Visualizer](https://leovoel.github.io/embed-visualizer/) - Live Discord embed designer with generated library snippets.
- [discord-interactions-python](https://github.com/discord/discord-interactions-python) - Official Discord helpers for verifying HTTP interaction signatures in Python (last activity 2024-04).
- [awesome-discord-communities](https://github.com/mhxion/awesome-discord-communities) - A curated list of Discord communities for programmers (last activity 2026-04).
- [jacc/awesome-discord](https://github.com/jacc/awesome-discord) - A curated list of Discord clients, bots, libraries, and related tools (last activity 2026-05).
- [Discord Library Comparison](https://libs.advaith.io) - Compares Discord libraries and their support for current API features.
- [Soheab/dpy-missing-features](https://github.com/Soheab/dpy-missing-features) - Notes on Discord API features that discord.py does not (yet) expose (last activity 2024-08).
- [Soheab/discord.py-tags](https://github.com/Soheab/discord.py-tags) - Overflow copies of long tags from the official discord.py Discord server (last activity 2024-12).
- [Soheab/dpy-badhosts](https://github.com/Soheab/dpy-badhosts) - Hosts the discord.py community generally warns against using for bots (last activity 2024-11).

## Forks and Wrappers

disnake, nextcord, Novus, pycord, and discord.py-message-components are discord.py forks. hikari, hata, interactions.py, and discord.http are independent wrappers, not drop-in replacements for discord.py.

- [disnake](https://github.com/DisnakeDev/disnake) - A modern, easy to use, feature-rich, and async-ready API wrapper for Discord written in Python (last activity 2026-08).
- [nextcord](https://github.com/nextcord/nextcord) - A Python wrapper for the Discord API forked from discord.py (last activity 2026-08).
- [Novus](https://github.com/Voxel-Fox-Ltd/Novus) - An asyncio Python wrapper around the Discord API, forked off of Rapptz's Discord.py (last activity 2026-07).
- [pycord](https://github.com/Pycord-Development/pycord) - A maintained fork of discord.py that wraps the Discord API (last activity 2026-08).
- [mccoderpy/discord.py-message-components](https://github.com/mccoderpy/discord.py-message-components) - A "fork" of discord.py library made by Rapptz with implementation of the Discord Message-Components & many other features by mccoderpy (last activity 2025-06).
- [hikari](https://github.com/hikari-py/hikari) - A Discord API wrapper for Python and asyncio, built independently of discord.py (last activity 2026-08).
- [interactions.py](https://github.com/interactions-py/interactions.py) - A highly extensible Discord bot framework for Python (last activity 2026-08).
- [hata](https://github.com/HuyaneMatsu/hata) - An async Discord API wrapper for Python, independent of discord.py (last activity 2026-08).
- [AlexFlipnote/discord.http](https://github.com/AlexFlipnote/discord.http) - An HTTP-interactions-first Discord library with optional gateway support (last activity 2026-08).

## Archived/Deprecated

- [thrzl/discord-ext-forms](https://github.com/thrzl/discord-ext-forms) - A simpler way to make forms, surveys, and reaction input using discord.py (last activity 2022-10).
- [Ext-Creators/discord-ext-events](https://github.com/Ext-Creators/discord-ext-events) - A discord.py extension with additional events (last activity 2021-07).
- [Ext-Creators/discord-ext-converters](https://github.com/Ext-Creators/discord-ext-converters) - A discord.py extension with a collection of useful converters (last activity 2021-03).
- [Ext-Creators/discord-ext-rx](https://github.com/Ext-Creators/discord-ext-rx) - A discord.py extension with a reactive events implementation (last activity 2020-08).
- [discord-py-ui/discord-ui](https://github.com/discord-py-ui/discord-ui) - A discord.py extension that allows you to create and manage buttons, slash commands, and more (last activity 2022-02).
- [PythonistaGuild/buttons](https://github.com/PythonistaGuild/buttons) - Archived interactive session and reaction-button paginator for discord.py (last activity 2021-06).
- [soosBot-com/Pagination](https://github.com/soosBot-com/Pagination) - Archived embed paginator library for discord.py 2.0 (last activity 2022-11).
- [Ext-Creators/discord-ext-ipc](https://github.com/Ext-Creators/discord-ext-ipc) - Archived discord.py IPC extension. Prefer discord-ext-ipcx (last activity 2021-08).
- [MiroslavRosenov/better-ipc](https://github.com/MiroslavRosenov/better-ipc) - Archived high-performance IPC library for discord.py. Prefer discord-ext-ipcx (last activity 2024-10).
- [EQUENOS/dislash.py](https://github.com/EQUENOS/dislash.py) - Archived slash-command and button wrapper from before discord.py 2.0 (last activity 2021-12).
- [woohyunjng/discord.py-components](https://github.com/woohyunjng/discord.py-components) - Archived unofficial components library from before native discord.py UI (last activity 2021-10).
- [Ext-Creators/discord-ext-alternatives](https://github.com/Ext-Creators/discord-ext-alternatives) - Archived discord.py extension with extra and alternative features (last activity 2021-04).
- [discordsuperutils/discord-super-utils](https://github.com/discordsuperutils/discord-super-utils) - Archived high-level helpers for common discord.py bot features (last activity 2022-10).
- [XuaTheGrate/slash_util](https://github.com/XuaTheGrate/slash_util) - Archived helper for adding application commands on early discord.py 2.0 (last activity 2022-02).
- [Ikusaba-san/dpy-ui](https://github.com/Ikusaba-san/dpy-ui) - Unmaintained prompt and pagination helpers. Prefer native views (last activity 2020-05).
- [wasi-master/dpylint](https://github.com/wasi-master/dpylint) - Unmaintained Pylint plugin for discord.py bot code (last activity 2022-03).
- [Rapptz/discord-ext-menus](https://github.com/Rapptz/discord-ext-menus) - Experimental reaction-menu helpers from before native views. Prefer discord-ext-pager or built-in UI (last activity 2022-05).
- [oliver-ni/discord-ext-menus-views](https://github.com/oliver-ni/discord-ext-menus-views) - Thin View layer over discord-ext-menus. Prefer native views or discord-ext-pager (last activity 2022-07).
<!-- END CONTENT -->

## Contributing

[Contributions of any kind welcome, just follow the guidelines](contributing.md)!

### Contributors

[Thanks goes to these contributors](https://github.com/kzndotsh/awesome-discordpy/graphs/contributors)!
