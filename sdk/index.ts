/// <reference lib="dom" />
/// <reference lib="dom.iterable" />

declare global {
  interface Window {
    RC: any;
  }
}

let SDK_IS_AUTHENTICATED = false;
const SDK_LOADED_END = "sdkLoadedEnd";

const isSDKAuthenticated = async () => {
  if (SDK_IS_AUTHENTICATED) {
    return true;
  }

  const res = await fetch(`${process.env.API_SERVER_URL}/api/userIsAuthed`, {
    credentials: "include",
  });
  const { user_is_authed } = await res.json();
  if (!user_is_authed) {
    const redirect_uri = encodeURIComponent(window.location.href);
    setTimeout(() => {
      window.location.href = `${process.env.API_SERVER_URL}/developers?redirect_uri=${redirect_uri}`;
    }, 50);
    return false;
  } else {
    SDK_IS_AUTHENTICATED = true;
    return true;
  }
};

// Fetches signed in users from the RC API using the given RC Personal Access
// Token
const getHubVisitsForToday = async () => {
  if (!(await isSDKAuthenticated())) {
    return;
  }

  const res = await fetch(
    `${process.env.API_SERVER_URL}/api/hubVisitsForToday`,
    {
      credentials: "include",
    }
  );
  const data = await res.json();
  return data;
};

// Calls the developer provided function when ready
const onLoad = (clientOnLoadCallback: () => void) => {
  // Tell parent rctv iframe that onLoad was called so it can stop its 30 second kill timer
  window.parent.postMessage(
    {
      type: SDK_LOADED_END,
    },
    "*"
  );

  // good to go, let's go
  clientOnLoadCallback();
};

window.RC = {
  onLoad,
  getHubVisitsForToday,
};
