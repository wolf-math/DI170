const getPosts = (userId) =>
  new Promise((resolve) => {
    setTimeout(() => {
      console.log('Posts Done!');
      resolve([
        { title: 'Article on Javascript', idArticle: 1, idUser: userId }
      ]);
    }, 1500);
  });

const getComments = (postId) =>
  new Promise((resolve) => {
    setTimeout(() => {
      console.log('Comments Done!');
      resolve([
        { title: 'Great Article', author: 'John' },
        { title: 'Interesting Article', author: 'Lea' }
      ]);
    }, 1500);
  });

const getLikes = (postId) =>
  new Promise((resolve) => {
    setTimeout(() => {
      console.log('Likes Done!');
      resolve(5);
    }, 1500);
  });

const getLatestPostActivity = async (userId) => {
  const posts = await getPosts(userId);
  const latestPost = posts[0];

  // Run comments and likes in parallel
  const [comments, likes] = await Promise.all([
    getComments(latestPost.idArticle),
    getLikes(latestPost.idArticle)
  ]);

  return { comments, likes };
};

// Fully async top-level execution
(async () => {
  try {
    const activity = await getLatestPostActivity(10);
    console.log('Everything:', activity);
  } catch (error) {
    console.error('Error fetching post activity:', error);
  }
})();
