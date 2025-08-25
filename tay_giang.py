<!DOCTYPE html>
<html lang="vi" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Website: Những Người Bảo Vệ Trẻ Của Trường Sơn</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
            height: 300px;
            max-height: 400px;
        }
        @media (min-width: 768px) {
            .chart-container {
                height: 400px;
            }
        }
        /* Add padding top to body to offset for sticky nav */
        body {
            padding-top: 70px;
        }
        .nav-link.active {
            color: #118AB2;
            font-weight: 700;
        }
    </style>
</head>
<body class="bg-gray-100 text-[#073B4C]">

    <!-- Color Palette: Energetic & Playful -->
    <!-- NEITHER Mermaid JS NOR SVG were used in this output. -->

    <nav class="fixed top-0 left-0 right-0 bg-white/90 backdrop-blur-sm shadow-md z-50">
        <div class="container mx-auto px-4 md:px-8">
            <div class="flex justify-between items-center h-16">
                <a href="#" class="text-xl font-bold text-[#073B4C]">Người Bảo Vệ Trẻ</a>
                <div class="hidden md:flex space-x-8">
                    <a href="#kho-bau" class="nav-link text-gray-600 hover:text-[#118AB2] transition-colors">Kho Báu</a>
                    <a href="#du-lieu" class="nav-link text-gray-600 hover:text-[#118AB2] transition-colors">Dữ Liệu</a>
                    <a href="#bao-dong" class="nav-link text-gray-600 hover:text-[#118AB2] transition-colors">Báo Động</a>
                    <a href="#giai-phap" class="nav-link text-gray-600 hover:text-[#118AB2] transition-colors">Giải Pháp</a>
                </div>
                <div class="md:hidden">
                    <button id="mobile-menu-button" class="text-gray-600 hover:text-[#118AB2] focus:outline-none">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path></svg>
                    </button>
                </div>
            </div>
        </div>
        <div id="mobile-menu" class="md:hidden hidden bg-white shadow-lg">
            <a href="#kho-bau" class="block py-2 px-4 text-sm text-gray-600 hover:bg-gray-100">Kho Báu</a>
            <a href="#du-lieu" class="block py-2 px-4 text-sm text-gray-600 hover:bg-gray-100">Dữ Liệu</a>
            <a href="#bao-dong" class="block py-2 px-4 text-sm text-gray-600 hover:bg-gray-100">Báo Động</a>
            <a href="#giai-phap" class="block py-2 px-4 text-sm text-gray-600 hover:bg-gray-100">Giải Pháp</a>
        </div>
    </nav>

    <div class="container mx-auto p-4 md:p-8">

        <header class="text-center mb-12 pt-8">
            <h1 class="text-4xl md:text-6xl font-black text-[#118AB2] mb-2">🌳 Những Người Bảo Vệ Trẻ Của Trường Sơn 🌳</h1>
            <p class="text-lg md:text-xl text-gray-600">Hành trình khám phá và bảo vệ kho báu thiên nhiên tại Tây Giang, Quảng Nam</p>
        </header>

        <main class="space-y-16">

            <section id="kho-bau" class="bg-white rounded-2xl shadow-xl p-6 md:p-8 text-center transform hover:scale-105 transition-transform duration-300">
                <h2 class="text-3xl font-bold text-[#FF6B6B] mb-4">🦄 KHO BÁU CỦA CHÚNG TA ĐANG GẶP NGUY HIỂM!</h2>
                <div class="md:flex items-center gap-8">
                    <div class="md:w-2/3 text-left">
                        <p class="text-lg mb-4">Câu chuyện bắt đầu từ **Sao La**, "Kỳ lân Châu Á", một báu vật chỉ có tại núi rừng Trường Sơn quê hương ta. Nhưng loài vật huyền thoại này đang ở mức **"Cực kỳ nguy cấp"**, với chưa đến 50 cá thể còn lại trong tự nhiên.</p>
                        <p class="text-lg">Sao La là lời nhắc nhở rằng kho báu thiên nhiên của chúng ta vô giá, và cũng rất mong manh. Bảo vệ Sao La cũng chính là bảo vệ ngôi nhà chung của chúng ta.</p>
                    </div>
                    <div class="md:w-1/3 mt-6 md:mt-0">
                        <img src="https://placehold.co/400x300/118AB2/FFFFFF?text=Sao+La" alt="Hình ảnh minh họa Sao La" class="rounded-lg shadow-md mx-auto">
                    </div>
                </div>
            </section>

            <section id="du-lieu" class="bg-white rounded-2xl shadow-xl p-6 md:p-8">
                <h2 class="text-3xl font-bold text-center text-[#06D6A0] mb-2">📊 TÂY GIANG: MỘT KHO BÁU VÔ GIÁ</h2>
                <p class="text-center text-gray-600 mb-8">Quê hương Tây Giang là một trong những trung tâm đa dạng sinh học quan trọng nhất Việt Nam, được công nhận trên toàn cầu. Các số liệu dưới đây cho thấy sự giàu có của hệ sinh thái nơi đây.</p>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-center mb-8">
                    <div class="bg-[#FFD166] p-6 rounded-lg shadow-md">
                        <p class="text-5xl font-extrabold text-white">67</p>
                        <p class="text-lg font-semibold text-white mt-2">Loài Quý Hiếm</p>
                    </div>
                    <div class="bg-[#06D6A0] p-6 rounded-lg shadow-md">
                        <p class="text-5xl font-extrabold text-white">540</p>
                        <p class="text-lg font-semibold text-white mt-2">Loài Thực Vật</p>
                    </div>
                    <div class="bg-[#118AB2] p-6 rounded-lg shadow-md">
                        <p class="text-5xl font-extrabold text-white">510</p>
                        <p class="text-lg font-semibold text-white mt-2">Loài Động Vật</p>
                    </div>
                </div>
                <div class="chart-container">
                    <canvas id="biodiversityChart"></canvas>
                </div>
                <p class="text-center text-sm text-gray-500 mt-4">Biểu đồ so sánh số lượng các nhóm loài được ghi nhận tại Tây Giang.</p>
            </section>

            <section id="bao-dong" class="bg-white rounded-2xl shadow-xl p-6 md:p-8">
                <h2 class="text-3xl font-bold text-center text-[#FF6B6B] mb-8">🚨 NHỮNG HỒI CHUÔNG BÁO ĐỘNG</h2>
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                    <div class="bg-red-50 p-6 rounded-lg border-l-4 border-red-500">
                        <h3 class="text-2xl font-bold mb-4">Dấu Chân Con Người</h3>
                        <ul class="space-y-3 list-inside">
                            <li class="flex items-start"><span class="text-2xl mr-3">🔥</span><span>**Phá rừng:** Mất đi "ngôi nhà" của các loài sinh vật.</span></li>
                            <li class="flex items-start"><span class="text-2xl mr-3">🗑️</span><span>**Ô nhiễm:** Rác thải nhựa và hóa chất làm hại đất và nước.</span></li>
                            <li class="flex items-start"><span class="text-2xl mr-3">🔫</span><span>**Săn bắt trái phép:** Đẩy các loài như Tê Tê đến bờ vực tuyệt chủng.</span></li>
                        </ul>
                    </div>
                    <div class="bg-blue-50 p-6 rounded-lg border-l-4 border-blue-500">
                        <h3 class="text-2xl font-bold mb-4">Cơn Sốt Của Hành Tinh</h3>
                        <div class="space-y-4 flow-diagram">
                            <div class="p-3 bg-white rounded-md shadow-sm text-center">
                                <p class="font-semibold">1. Phát thải khí nhà kính toàn cầu</p>
                                <p class="text-sm">(từ nhà máy, xe cộ...)</p>
                            </div>
                            <div class="text-center text-2xl font-bold text-[#118AB2]">↓</div>
                            <div class="p-3 bg-white rounded-md shadow-sm text-center">
                                <p class="font-semibold">2. Hiệu ứng nhà kính & Nóng lên toàn cầu</p>
                            </div>
                            <div class="text-center text-2xl font-bold text-[#118AB2]">↓</div>
                            <div class="p-3 bg-white rounded-md shadow-sm text-center">
                                <p class="font-semibold">3. Thời tiết cực đoan & Mưa lớn bất thường</p>
                            </div>
                             <div class="text-center text-2xl font-bold text-[#FF6B6B]">↓</div>
                            <div class="p-3 bg-red-100 border border-red-400 rounded-md shadow-sm text-center">
                                <p class="font-bold text-red-700">4. HIỂM HỌA: SẠT LỞ ĐẤT TẠI TÂY GIANG</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            
            <section id="giai-phap" class="bg-white rounded-2xl shadow-xl p-6 md:p-8">
                <h2 class="text-3xl font-bold text-center text-[#FFD166] mb-8">💡 TRỞ THÀNH MỘT PHẦN CỦA GIẢI PHÁP!</h2>
                <p class="text-center text-gray-600 mb-8 max-w-3xl mx-auto">Thay đổi lớn lao luôn bắt đầu từ những hành động nhỏ bé. Mỗi chúng ta đều có thể trở thành một Người Bảo Vệ Trẻ của Trường Sơn.</p>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <div class="bg-gray-50 p-6 rounded-lg text-center transform hover:-translate-y-2 transition-transform duration-300">
                        <div class="text-5xl mb-4">🔌</div>
                        <h3 class="text-xl font-bold mb-2">Tiết kiệm năng lượng</h3>
                        <p>Tắt đèn, rút phích cắm các thiết bị điện khi không sử dụng.</p>
                    </div>
                    <div class="bg-gray-50 p-6 rounded-lg text-center transform hover:-translate-y-2 transition-transform duration-300">
                        <div class="text-5xl mb-4">🛍️</div>
                        <h3 class="text-xl font-bold mb-2">Giảm rác thải nhựa</h3>
                        <p>Dùng túi vải, bình nước cá nhân thay cho đồ nhựa dùng một lần.</p>
                    </div>
                    <div class="bg-gray-50 p-6 rounded-lg text-center transform hover:-translate-y-2 transition-transform duration-300">
                        <div class="text-5xl mb-4">🚲</div>
                        <h3 class="text-xl font-bold mb-2">Di chuyển xanh</h3>
                        <p>Ưu tiên đi bộ hoặc đi xe đạp cho những quãng đường gần.</p>
                    </div>
                    <div class="bg-gray-50 p-6 rounded-lg text-center transform hover:-translate-y-2 transition-transform duration-300">
                        <div class="text-5xl mb-4">🌱</div>
                        <h3 class="text-xl font-bold mb-2">Trồng cây xanh</h3>
                        <p>Mỗi cây xanh được trồng là một "nhà máy" lọc không khí tí hon.</p>
                    </div>
                    <div class="bg-gray-50 p-6 rounded-lg text-center transform hover:-translate-y-2 transition-transform duration-300">
                        <div class="text-5xl mb-4">🗣️</div>
                        <h3 class="text-xl font-bold mb-2">Nói không với sản phẩm ĐVHD</h3>
                        <p>Không mua bán, sử dụng các sản phẩm từ động vật hoang dã.</p>
                    </div>
                    <div class="bg-gray-50 p-6 rounded-lg text-center transform hover:-translate-y-2 transition-transform duration-300">
                        <div class="text-5xl mb-4">💌</div>
                        <h3 class="text-xl font-bold mb-2">Lan tỏa thông điệp</h3>
                        <p>Chia sẻ những điều bạn biết cho gia đình và bạn bè.</p>
                    </div>
                </div>
            </section>

        </main>

        <footer class="text-center mt-12 py-6 border-t border-gray-300">
            <p class="text-2xl font-bold text-[#073B4C]">HÀNH ĐỘNG NHỎ, THAY ĐỔI LỚN.</p>
            <p class="text-gray-600">TƯƠNG LAI CỦA TÂY GIANG NẰM TRONG TAY BẠN!</p>
        </footer>

    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function () {
            // Chart.js implementation
            const ctx = document.getElementById('biodiversityChart').getContext('2d');
            const labels = ['Thực vật', 'Thú', 'Chim', ['Bò sát &', 'Lưỡng cư'], 'Côn trùng'];
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Số Lượng Loài',
                        data: [540, 40, 137, 94, 299],
                        backgroundColor: ['#06D6A0', '#FFD166', '#118AB2', '#FF6B6B', '#073B4C'],
                        borderColor: ['#06D6A0', '#FFD166', '#118AB2', '#FF6B6B', '#073B4C'],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: { beginAtZero: true, grid: { color: '#e5e7eb' }, ticks: { color: '#4b5563' } },
                        x: { grid: { display: false }, ticks: { color: '#4b5563', font: { size: 14 } } }
                    },
                    plugins: {
                        legend: { display: false },
                        title: {
                            display: true,
                            text: 'Sự Đa Dạng Các Loài tại Tây Giang',
                            font: { size: 18, weight: 'bold' },
                            color: '#073B4C',
                            padding: { top: 10, bottom: 20 }
                        },
                        tooltip: {
                            callbacks: {
                                title: function(tooltipItems) {
                                    const item = tooltipItems[0];
                                    let label = item.chart.data.labels[item.dataIndex];
                                    return Array.isArray(label) ? label.join(' ') : label;
                                }
                            }
                        }
                    }
                }
            });

            // Mobile menu toggle
            const mobileMenuButton = document.getElementById('mobile-menu-button');
            const mobileMenu = document.getElementById('mobile-menu');
            mobileMenuButton.addEventListener('click', () => {
                mobileMenu.classList.toggle('hidden');
            });

            // Active link highlighting on scroll
            const sections = document.querySelectorAll('section');
            const navLinks = document.querySelectorAll('.nav-link');

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        navLinks.forEach(link => {
                            link.classList.remove('active');
                            if (link.getAttribute('href').substring(1) === entry.target.id) {
                                link.classList.add('active');
                            }
                        });
                    }
                });
            }, { threshold: 0.5 });

            sections.forEach(section => {
                observer.observe(section);
            });
        });
    </script>

</body>
</html>
