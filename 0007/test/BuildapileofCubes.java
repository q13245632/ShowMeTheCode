//自己的解法
public class ASum {
	public static long findNb(long m) {
		System.out.println(m);
		long n = (long) (Math.sqrt(Math.sqrt(m) * 8 + 1) - 1)/2;
		if (n*n*(n+1)*(n+1)/4 != m) {
			n = -1;
		}
		return n;
	}
}
//测试集
import static org.junit.Assert.*;
import org.junit.Test;
public class ASumTest {
	@Test
	public void test1() {
		assertEquals(2022, ASum.findNb(4183059834009L));
	}
	@Test
	public void test2() {
		assertEquals(-1, ASum.findNb(24723578342962L));
	}
	@Test
	public void test3() {
		assertEquals(4824, ASum.findNb(135440716410000L));
	}
	@Test
	public void test4() {
		assertEquals(3568, ASum.findNb(40539911473216L));
	}
}

public class ASum {
  
  public static long findNb(long m) {
    long mm = 0, n = 0;
    while (mm < m) mm += ++n * n * n;
    return mm == m ? n : -1;
  }  
}