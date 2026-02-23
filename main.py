message = f"<b>{event.name}</b> - {event.location} ({event.date})"  useEffect(() => {
    fetch("http://127.0.0.1:8000/events")
      .then((res) => res.json())
      .then((data) => setEvents(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Smart Event Management</h1>

      <h2>Upcoming Events</h2>
      <ul>
        {events.map((event) => (
          <li key={event.id}>
            <b>{event.name}</b> – {event.location} ({event.date})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

