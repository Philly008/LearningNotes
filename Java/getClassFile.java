import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.FilenameFilter;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;
import java.util.List;

public class getClassFile {
	String subject = "";
	String sourceDir = "";
	String objectDir = "";

	public void init() {
		// NIP_REPORT_3.0.0.0,NIP_QUERY,NIP_CUS_3.0,NIP_3.5.0.0,NIP_TONGBU_3.5.0.0,NIP_WeiMon
		subject = "NIP_local";
		//subject = "NIP_3.5_release";
		sourceDir = this.getSourceDir(subject);
		objectDir = "E:/export/javaclasses/" + this.getFormatDate() + "/NIP/";
		//objectDir = "E:/export/javaclasses/NIP_3.5_release/" + this.getFormatDate() + "/NIP_3.5_release/";
	}

	private String getSourceDir(String subject) {
		String fileContext = "";
		if ("NIP_REPORT_local".equals(subject)) {
			//fileContext = "E:/3.5_release/NIP_3.5.0.0_release/WebContent/";
			fileContext = "E:/newworkspace/windows/local/NIP_REPORT_local/WebContent/";
		} else if ("NIP_local".equals(subject)) {
			fileContext = "E:/newworkspace/windows/local/NIP_local/WebContent/";
		} else if ("NIP_TONGBU_local".equals(subject)) {
			fileContext = "E:/newworkspace/windows/local/NIP_TONGBU_local/WebContent/";
		} else { 
			fileContext = "e:/xxt3/trunk/web/";
		}
		return fileContext;
	}

	public static void main(String[] args) {
		new getClassFile().run();
	}

	private void run() {
		this.init();
		int suc_num = 0;
		int fail_num = 0;
		int suc_dir_num = 0;
		int fail_dir_num = 0;
		int not_file_num = 0;
		try {
			BufferedReader br = new BufferedReader(new FileReader("E:/�����ļ�.txt"));
			String r = br.readLine();
			String r_init = "";
			while (r != null) {
				r = r.trim();
				if (r.indexOf(".") < 0 && !r.endsWith("*")) {
					System.out.println(r + "�����������ļ�·����");
					not_file_num++;
					r = br.readLine();
					continue;
				}
				if (r.startsWith("web/")) {
					r = r.substring(4);
				}
				r = r.replaceAll("\\\\", "/");
				r_init = r;
				boolean flag = true;

				if (r.endsWith("*.java")) { // java�ļ�ȫĿ¼
					r = r.replaceAll("src/", "/");
					r = r.replaceAll(".java", ".class");
					r = "WEB-INF/classes/" + r;
					List<String> list = FileViewer1.getListFiles(sourceDir + r.substring(0, r.lastIndexOf("/") + 1), "",
							true);
					for (Iterator<String> i = list.iterator(); i.hasNext();) {
						String temp = (String) i.next();
						if (temp.indexOf(".svn") > 0) {
							continue;
						}
						temp = temp.replaceAll("\\\\", "/");
						flag = !flag ? false : CopyFile(temp, objectDir + temp.replaceAll(sourceDir, ""));
					}
					if (flag) {
						suc_dir_num++;
					} else {
						fail_dir_num++;
					}
				} else if (r.endsWith("*")) { // �����ļ�ȫĿ¼
					List<String> list = FileViewer1.getListFiles(sourceDir + r.substring(0, r.lastIndexOf("/") + 1), "",
							true);
					for (Iterator<String> i = list.iterator(); i.hasNext();) {
						String temp = (String) i.next();
						if (temp.indexOf(".svn") > 0) {
							continue;
						}
						temp = temp.replaceAll("\\\\", "/");
						flag = !flag ? false : CopyFile(temp, objectDir + temp.replaceAll(sourceDir, ""));
					}
					if (flag) {
						suc_dir_num++;
					} else {
						fail_dir_num++;
					}
				} else if (r.endsWith(".java")) {
					r = r.replaceAll("src/", "/");
					r = r.replaceAll(".java", ".class");
					r = "WEB-INF/classes/" + r;
					String[] names = new java.io.File(sourceDir + r.substring(0, r.lastIndexOf("/") + 1))
							.list(new ScriptFilenameFilter(".class"));
					for (int i = 0; i < names.length; i++) {
						if (names[i].startsWith(r.substring(r.lastIndexOf("/") + 1, r.lastIndexOf(".")))) {
							flag = !flag ? false : CopyFile(sourceDir + r.substring(0, r.lastIndexOf("/") + 1)
									+ names[i], objectDir + r.substring(0, r.lastIndexOf("/") + 1) + names[i]);
						}
					}
					if (flag) {
						suc_num++;
					} else {
						System.out.println(sourceDir + r + " Դ�ļ������ڻ��ƹ��̳����쳣!");
						fail_num++;
					}
				} else if (r.endsWith(".htm")) {
					if (!r.startsWith("WEB-INF/") && !r.startsWith("velocity/")) {
						r = "velocity/" + r;
					}
					if (!r.startsWith("WEB-INF/")) {
						r = "WEB-INF/" + r;
					}
					flag = CopyFile(sourceDir + r, objectDir + r);
					if (flag) {
						suc_num++;
					} else {
						// System.out.println(sourceDir + r_init +
						// "��htm�ļ���������ԭʼ·����Ѱ");
						flag = CopyFile(sourceDir + r_init, objectDir + r_init);
						if (flag) {
							suc_num++;
						} else {
							System.out.println(sourceDir + r_init + " Դ�ļ������ڻ��ƹ��̳����쳣!");
							fail_num++;
						}
					}
				} else {
					flag = CopyFile(sourceDir + r, objectDir + r);
					if (flag) {
						suc_num++;
					} else {
						System.out.println(sourceDir + r + " Դ�ļ������ڻ��ƹ��̳����쳣!");
						fail_num++;
					}
				}
				r = br.readLine();
			}
			System.out.println("��ȡ�ļ�������������" + (suc_dir_num + fail_dir_num + suc_num + fail_num + not_file_num)
					+ "�����и��Ƴɹ�Ŀ¼" + suc_dir_num + "������ʧ��Ŀ¼" + fail_dir_num + "�����Ƴɹ��ļ�" + suc_num + "������ʧ���ļ�" + fail_num
					+ "���ų��������ļ�·��" + not_file_num);
		} catch (Exception e) {
			e.printStackTrace();
			System.out.println("�ļ���ȡ������");
		}

	}

	public class ScriptFilenameFilter implements FilenameFilter {
		private String suffix;

		public ScriptFilenameFilter(String suffix) {
			this.suffix = suffix;
		}

		public boolean accept(File dir, String name) {
			if (name.endsWith(suffix)) {
				return true;
			}
			return false;
		}

	}

	public boolean CopyFile(String oldFilePath, String newFilePath) {
		File dirFile;
		boolean bFile;
		try {
			if (oldFilePath == null || oldFilePath.trim().length() == 0 || newFilePath == null
					|| newFilePath.trim().length() == 0) {
				System.out.println("·��Ϊ��");
				return false;

			}
			// ���ԭ�ļ����ж��ļ��Ƿ����
			File sfile = new File(oldFilePath);
			if (sfile.exists() == false) {
				// System.out.println(oldFilePath + " ԭ�ļ�������");
				return false;
			}
			// �жϵڶ���·�����Ƿ���� �����ھʹ������ļ���
			dirFile = new File(newFilePath.substring(0, newFilePath.lastIndexOf("/")));
			bFile = dirFile.exists();
			if (bFile == false) {
				// System.out.println("�ļ�Ŀ¼�����ڣ����ڴ���Ŀ¼");
				bFile = dirFile.mkdirs();
				if (bFile == true) {
					// System.out.println("�����ɹ�");
				} else {
					System.out.println(newFilePath.substring(0, newFilePath.lastIndexOf("/")) + " Ŀ¼�������ɹ�");
					System.exit(0);
				}
			}
			// ��Ŀ¼����copy�ļ�
			// System.out.println(oldFilePath + " �ļ��Ѿ����ڣ��������ļ���COPY�ļ�");
			String filename = sfile.getName();
			File tfile = new File(dirFile, filename);
			RandomAccessFile rdtfile = new RandomAccessFile(tfile, "rw");
			RandomAccessFile rdsfile = new RandomAccessFile(sfile, "r");
			byte[] contents = new byte[(int) rdsfile.length()];
			rdsfile.read(contents);
			rdsfile.close();

			rdtfile.write(contents);
			rdtfile.close();
			// System.out.println(newFilePath + " �ļ����Ƴɹ�!");
		} catch (Exception e) {
			e.printStackTrace();
			System.out.println(oldFilePath + "����ʧ�ܣ��׳��쳣��");
			return false;
		}
		return true;
	}

	public String getFormatDate() {
		return new SimpleDateFormat("yyyyMMddHHmm").format(new Date());
	}

}

class FileViewer1 {
	public static List<String> fileList = new ArrayList<String>();

	/**
	 * 
	 * @param path
	 *            �ļ�·��
	 * @param suffix
	 *            ��׺��
	 * @param isdepth
	 *            �Ƿ������Ŀ¼
	 * @return
	 */
	public static List<String> getListFiles(String path, String suffix, boolean isdepth) {
		fileList = new ArrayList<String>();
		File file = new File(path);
		return listFile(file, suffix, isdepth);
	}

	public static List<String> listFile(File f, String suffix, boolean isdepth) {
		// ��Ŀ¼��ͬʱ��Ҫ������Ŀ¼
		if (f.isDirectory() && isdepth == true) {
			File[] t = f.listFiles();
			for (int i = 0; i < t.length; i++) {
				listFile(t[i], suffix, isdepth);
			}
		} else {
			String filePath = f.getAbsolutePath();

			// System.out.println("suffix = "+suffix);
			if (suffix == "" || suffix == null) {
				// ��׺��Ϊnull��Ϊ�����ļ�
				// System.out.println("----------------");
				fileList.add(filePath);
			} else {
				int begIndex = filePath.lastIndexOf(".");// ���һ��.(����׺��ǰ���.)������
				String tempsuffix = "";

				if (begIndex != -1) {// ��ֹ���ļ���ȴû�к�׺���������ļ�
					tempsuffix = filePath.substring(begIndex + 1, filePath.length());
				}

				if (tempsuffix.equals(suffix)) {
					fileList.add(filePath);
				}
			}

		}

		return fileList;
	}

	/**
	 * ����׷���ļ���ʹ��FileWriter
	 * 
	 * @param fileName
	 * @param content
	 */
	public static void appendMethod(String fileName, String content) {
		try {
			// ��һ��д�ļ��������캯���еĵڶ�������true��ʾ��׷����ʽд�ļ�
			FileWriter writer = new FileWriter(fileName, true);
			writer.write(content + "\r\n");
			writer.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
