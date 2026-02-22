self.addEventListener('install',()=>{

    self.skipWaiting();

});

self.addEventListener('fetch',e=>{
    e.respondWith(
        fetch(e.request).catch(()=>{})
    );
});
// service-worker.js 예시
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      // 1. 캐시에 있으면 캐시된 응답 반환
      // 2. 캐시에 없으면 네트워크에서 가져옴
      // 3. 네트워크도 실패하면 빈 응답이라도 반환 (TypeError 방지)
      return response || fetch(event.request).catch(() => {
        return new Response('Network error occurred', {
          status: 408,
          statusText: 'Network error'
        });
      });
    })
  );
});
