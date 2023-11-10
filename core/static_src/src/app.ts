import "vite/modulepreload-polyfill";
import * as img from "./slash-commands/img";
import * as appIndex from "./slash-commands/appIndex";
import * as chyron from "./slash-commands/chyron";

const SLASH_COMMAND_MAPPING: Record<string, any> = {
  img,
  appIndex,
  chyron,
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
      const res = content.match(/^\/(\w+) (.*)$/);
      if (res) {
        const [_, slashCommand, slashCommandArgs] = res;
        const slashCommandFn = SLASH_COMMAND_MAPPING[slashCommand];
        if (slashCommandFn) {
          slashCommandFn.default(slashCommandArgs);
        }
      }
    });
  }, 1000);
});
