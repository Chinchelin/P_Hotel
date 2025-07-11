// Create floating bubbles background effect
document.addEventListener('DOMContentLoaded', function() {
    const bubblesContainer = document.getElementById('bubbles');
    
     //BURBUJAS
    for (let i = 0; i < 15; i++) {
        const bubble = document.createElement('div');
        bubble.classList.add('bubble');
        
        // EL SIZE
        const size = Math.random() * 90 + 10;
        bubble.style.width = `${size}px`;
        bubble.style.height = `${size}px`;
        
        // EL RAMDOM POSITION
        bubble.style.left = `${Math.random() * 100}%`;
        
        //ANIMACION DEL RANDOM (10-30 seconds)
        const duration = Math.random() * 20 + 10;
        bubble.style.animationDuration = `${duration}s`;
        
        // Random animation delay (0-5 seconds)
        bubble.style.animationDelay = `${Math.random() * 5}s`;
        
        bubblesContainer.appendChild(bubble);
    }
    
    // Menu navigation functionality
    const menuItems = document.querySelectorAll('.menu-item');
    const formSections = document.querySelectorAll('.form-section');
    
    menuItems.forEach(item => {
        item.addEventListener('click', function(e) {
            // Skip if item is a link
            if (this.tagName === 'A') return;
            
            e.preventDefault();
            
            // Remove active class from all menu items
            menuItems.forEach(i => i.classList.remove('active'));
            
            // Add active class to clicked item
            this.classList.add('active');
            
            // Hide all form sections
            formSections.forEach(section => section.classList.remove('active'));
            
            // Show corresponding section
            const sectionId = this.getAttribute('data-section') + 'Section';
            const targetSection = document.getElementById(sectionId);
            
            if (targetSection) {
                targetSection.classList.add('active');
                
                // Add animation
                targetSection.classList.add('animate__animated', 'animate__fadeIn');
                setTimeout(() => {
                    targetSection.classList.remove('animate__animated', 'animate__fadeIn');
                }, 500);
            }
        });
    });
    
    // Add hover effect to menu items
    menuItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.classList.add('animate__animated', 'animate__pulse');
            setTimeout(() => {
                this.classList.remove('animate__animated', 'animate__pulse');
            }, 1000);
        });
    });
    
    // Add click effect to widgets
    const widgets = document.querySelectorAll('.widget');
    widgets.forEach(widget => {
        widget.addEventListener('click', function() {
            this.classList.add('animate__animated', 'animate__headShake');
            setTimeout(() => {
                this.classList.remove('animate__animated', 'animate__headShake');
            }, 1000);
        });
    });
    
    // Form buttons functionality
    document.getElementById('addProductBtn').addEventListener('click', function(e) {
        e.preventDefault();
        alert('Funcionalidad para agregar nuevo producto');
        // Aquí iría la lógica para mostrar el formulario de nuevo producto
    });
    
    document.getElementById('addTrainingBtn').addEventListener('click', function(e) {
        e.preventDefault();
        alert('Funcionalidad para programar nueva capacitación');
        // Aquí iría la lógica para mostrar el formulario de nueva capacitación
    });
    
    document.getElementById('addBrandBtn').addEventListener('click', function(e) {
        e.preventDefault();
        alert('Funcionalidad para agregar nueva marca');
        // Aquí iría la lógica para mostrar el formulario de nueva marca
    });
    
    // Table actions functionality
    document.querySelectorAll('.table-btn-edit').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const row = this.closest('tr');
            const itemId = row.querySelector('td:first-child').textContent;
            alert(`Editando: ${itemId}`);
            // Aquí iría la lógica para editar el elemento
        });
    });
    
    document.querySelectorAll('.table-btn-delete').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const row = this.closest('tr');
            const itemId = row.querySelector('td:first-child').textContent;
            if (confirm(`¿Estás seguro de eliminar ${itemId}?`)) {
                row.remove();
                alert(`${itemId} eliminado correctamente`);
            }
        });
    });
    
    // Search functionality
    const searchInput = document.querySelector('.search-box input');
    searchInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();
        
        // Search in tables
        document.querySelectorAll('.data-table tbody tr').forEach(row => {
            const rowText = row.textContent.toLowerCase();
            row.style.display = rowText.includes(searchTerm) ? '' : 'none';
        });
        
        // Search in activity list
        document.querySelectorAll('.activity-item').forEach(item => {
            const itemText = item.textContent.toLowerCase();
            item.style.display = itemText.includes(searchTerm) ? '' : 'none';
        });
    });
    
    // Simulate loading pending invoices
    setTimeout(() => {
        const pendingInvoices = Math.floor(Math.random() * 10);
        const badge = document.getElementById('pendingInvoices');
        if (badge) {
            badge.textContent = pendingInvoices;
            if (pendingInvoices > 0) {
                badge.style.display = 'inline-block';
                badge.style.padding = '2px 6px';
                badge.style.borderRadius = '10px';
                badge.style.backgroundColor = 'var(--primary-dark)';
                badge.style.color = 'white';
                badge.style.fontSize = '0.7rem';
            }
        }
    }, 1000);
    
    // User profile dropdown functionality (example)
    const userProfile = document.querySelector('.user-profile');
    if (userProfile) {
        userProfile.addEventListener('click', function() {
            alert('Menú de usuario desplegado\nAquí irían las opciones de perfil, configuración y cerrar sesión');
        });
    }
});