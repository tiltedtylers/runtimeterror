import React,{useEffect,useState} from 'react'
import { Table } from 'react-bootstrap';
import axios from 'axios'

const Dashboard = () => {
    const [data, setData] = useState(null)
    useEffect(()=> {
        async function getData(){
            fetch("http://localhost:8090/deals").then(res => {
                console.log(res.data)
                setData(res.data)
            })
        }
        getData()
    },[])
    return (
        <div>
            <Table>
            {data}
            </Table>
        </div>
    )
}

export default Dashboard;