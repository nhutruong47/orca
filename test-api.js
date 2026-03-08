const fetch = require('node-fetch');

async function test() {
    try {
        const reg = await fetch('https://orca-backend-gyha.onrender.com/api/auth/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: "testnode2", password: "123", fullName: "Node Test" })
        });
        console.log("Reg:", reg.status);

        const login = await fetch('https://orca-backend-gyha.onrender.com/api/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: "testnode2", password: "123" })
        });
        const { token } = await login.json();
        console.log("Token:", !!token);

        const team = await fetch('https://orca-backend-gyha.onrender.com/api/teams', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ name: "Team Node", description: "Desc Node" })
        });

        console.log("Team Status:", team.status);
        const body = await team.text();
        console.log("Team Body:", body);
    } catch (err) {
        console.log("Error:", err);
    }
}
test();
