export default function (appIndex: string) {
  let appIndexNum = parseInt(appIndex);
  if (Number.isInteger(appIndexNum) && appIndexNum >= 0) {
    window.location.href = `/app/${appIndexNum}`;
  }
}
