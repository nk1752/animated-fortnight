const url =
    "http://api.weatherapi.com/v1/current.json?key=" +
    process.env.WEATHER_API_KEY +
    "&q=" +
    city +
    "&aqi=yes";

  const res = await fetch(url, {
    method: "GET",
    mode: "cors",
    next: {
      revalidate: 0,
    },
    headers: {
      "Content-Type": "application/json",
    },
  });
WEATHER_API_KEY=ef50495ff7bd48708b0142219232003

https://chatgpt.com/share/672ca9a4-47a4-8008-964f-ef0687c86934
