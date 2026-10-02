async function loadPosts() {
    try {
        const response = await fetch("http://localhost/api/posts/");
        const posts = await response.json();

        const postsContainer = document.getElementById("posts");
        postsContainer.innerHTML = "";

        for (const post of posts) {
            const commentsResponse = await fetch(
                `http://localhost/api/posts/${post.id}/comments/`
            );

            const comments = await commentsResponse.json();

            const postDiv = document.createElement("div");
            postDiv.className = "post";

            let commentsHTML = "";

            comments.forEach(comment => {
                commentsHTML += `
                    <div class="comment">
                        <strong>${comment.author}</strong>
                        <p>${comment.content}</p>
                    </div>
                `;
            });

            postDiv.innerHTML = `
                <h2>${post.title}</h2>
                <p>${post.content}</p>

                <small>Author: ${post.author}</small>

                <h3>Comments</h3>
                ${commentsHTML || "<p>No comments yet.</p>"}
            `;

            postsContainer.appendChild(postDiv);
        }

    } catch (error) {
        console.error("Error loading blog:", error);
    }
}