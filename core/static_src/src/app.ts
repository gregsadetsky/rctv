import "vite/modulepreload-polyfill";
import * as img from "./slash-commands/img";
import * as appIndex from "./slash-commands/appIndex";
import * as ticker from "./slash-commands/ticker";

const SLASH_COMMAND_MAPPING: Record<string, any> = {
  img,
  appIndex,
  ticker,
};

document.addEventListener("DOMContentLoaded", function () {
  // start interval,
  // get all unprocessed zulip messages from the server
  // process them here.
  setInterval(async () => {
    const res = await fetch("/internal-api/get_unprocessed_zulip_messages");
    const { unprocessed_zulip_messages } = await res.json();
    unprocessed_zulip_messages.forEach((message: any) => {
      const { content } = message.message;
      // match:
      // - @rctv /img someurl
      // - /img someurl
      const res = content.match(/^(@\*\*[^\*]+\*\* |)\/(\w+) (.*)$/);
      if (res) {
        const [_, __, slashCommand, slashCommandArgs] = res;
        const slashCommandFn = SLASH_COMMAND_MAPPING[slashCommand];
        if (slashCommandFn) {
          slashCommandFn.default(slashCommandArgs);
        }
      }
    });
  }, 1000);
});
