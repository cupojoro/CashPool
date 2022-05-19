function connect(){
    console.log("JS");
    console.log(window.location.href);
    console.log(LINK_TOKEN);
    const handler = Plaid.create({
      token: LINK_TOKEN,
      onSuccess: (public_token, metadata) => {
        console.log("SUCCESS PUBLIC TOKEN");
        console.log(public_token);
      },
      onLoad: () => {},
      onExit: (err, metadata) => {
        console.log("ERROR");
        console.log(err);
      },
      onEvent: (eventName, metadata) => {
        console.log("EVENT");
        console.log(eventName);
      }
    });

    handler.open();
}