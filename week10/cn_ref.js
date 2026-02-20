const weather = {
  lat: 52.2297,
  lon: 21.0122,
  timezone: 'Europe/Warsaw',
  timezone_offset: 3600,
  data: [
    {
      dt: 1645888976,
      sunrise: 1645853361,
      sunset: 1645891727,
      temp: 279.13,
      feels_like: 276.44,
      pressure: 1029,
      humidity: 64,
      dew_point: 272.88,
      uvi: 0.06,
      clouds: 0,
      visibility: 10000,
      wind_speed: 3.6,
      wind_deg: 340,
      weather: [
        {
          id: 800,
          main: 'Clear',
          description: 'clear sky',
          icon: '01d'
        }
      ]
    }
  ]
};

const weather2 = { ...weather };
weather2.timezone_offset = 'z';

weather2.data[0].sunrise = 0;
// weather2['data'][0]['sunrise']

// console.log(weather);
// console.log(weather2);

console.log(weather === weather2); //false
console.log(weather.data === weather2.data); //true

const weather3 = structuredClone(weather);

console.log(weather === weather3); // false
console.log(weather.data === weather3.data); // false

const weather4 = [...weather.data];
