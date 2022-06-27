// ul = document.getElementById('timeline-posts');
// list = document.createDocumentFragment();

fetch('http://127.0.0.1:5000/api/timeline_post')
.then((response) =>{return response.json()})
.then(data => {appendData(data)});

function appendData(data){
        for(var i=0; i<data.timeline_posts.length; i+=1){
            let timeline_post = data.timeline_posts[i];
            let  timelinediv = document.getElementById('timeline-posts');
            let name = document.createElement('name');
            let email = document.createElement('email');
            let content = document.createElement('content');
            let created_at = document.createElement('created_at');
            // var div = document.createElement("div");

            // div.innerHTML = `Name: ${timeline_post.name}
            //                 Email: ${timeline_post.email}
            //                 content: ${timeline_post.content}
            //                 created_at: ${timeline_post.created_at}`;
            name.innerHTML = `Name: ${timeline_post.name} <br />`;
            email.innerHTML = `Email: ${timeline_post.email} <br />`;
            content.innerHTML = `Content: ${timeline_post.content} <br />`;
            created_at.innerHTML = `Created at: ${timeline_post.created_at} <br /><br />`;

            timelinediv.appendChild(name);
            timelinediv.appendChild(email);
            timelinediv.appendChild(content);
            timelinediv.appendChild(created_at);
            
            // list.appendChild(li);
        };
}
// ul.appendChild(list);


const form = document.getElementById('form');
 
form.addEventListener('submit', function(e) {
    e.preventDefault();
    const data = new FormData();
    data.append("name", document.getElementById("user_name").value);
    data.append("email", document.getElementById("user_email").value);
    data.append("content", document.getElementById("user_content").value);
    fetch('http://127.0.0.1:5000/api/timeline_post', {
    method: 'POST',
    body: data,
    })
    location.reload();
})

// var mainContainer = document.getElementById('timeline-posts');
// list = document.createDocumentFragment();


