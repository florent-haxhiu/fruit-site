import axios from "axios"
import { useState, useEffect } from "react"

const homePage = () => {

  const [data, setData] = useState([]);

  useEffect(() => {
    const getData = () => {
      const { data } = axios.get("https://www.fruityvice.com/api/fruit/all/")
      console.log(data)
      setData(data)
    }
    getData()
  }, [])

  return (
    <div>
      <h1>Home Page</h1>
      <p>This is the home page</p>
    </div>
  )
}

export default homePage