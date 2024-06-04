CREATE TABLE `pegawai` (
  `id` int(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
  `nama` varchar(255) NOT NULL,
  `nip` varchar(255) NOT NULL,
  `tgl_lahir` date NOT NULL,
  `pangkat` varchar(255) NOT NULL,
  `golongan` varchar(255) NOT NULL,
  `jabatan` varchar(255) NOT NULL
)